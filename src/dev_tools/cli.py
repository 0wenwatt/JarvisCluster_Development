#!/usr/bin/env python3
"""
Jarvis Development Tools CLI

Command-line interface for using the development tools.
Provides commands for crawling, metadata management, and code querying.
"""

import sys
import argparse
import json
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from crawler import FileCrawler
from metadata_manager import MetadataManager
from query_interface import CodebaseQueryInterface


def cmd_crawl(args):
    """Crawl a directory and collect file information"""
    print(f"Crawling directory: {args.path}")
    
    crawler = FileCrawler(
        root_path=args.path,
        max_file_size=args.max_size * 1024 * 1024  # Convert MB to bytes
    )
    
    # Crawl with progress
    def progress_callback(file_path):
        if args.verbose:
            print(f"  Processing: {file_path}")
    
    files = crawler.crawl(update_callback=progress_callback if args.verbose else None)
    
    print(f"\nCrawl complete!")
    print(f"Total files: {len(files)}")
    
    # Get statistics
    stats = crawler.get_statistics()
    print(f"\nStatistics:")
    print(f"  Total files: {stats['total_files']}")
    print(f"  Total size: {stats['total_size']:,} bytes")
    print(f"  Total lines: {stats['total_lines']:,}")
    print(f"  Text files: {stats['text_files']}")
    print(f"  Binary files: {stats['binary_files']}")
    
    # Output to file if requested
    if args.output:
        output_data = {
            'files': {path: info.to_dict() for path, info in files.items()},
            'statistics': stats,
            'tree': crawler.get_tree_structure()
        }
        
        with open(args.output, 'w') as f:
            json.dump(output_data, f, indent=2)
        print(f"\nResults saved to: {args.output}")
    
    return 0


def cmd_metadata(args):
    """Manage metadata and check for changes"""
    metadata_mgr = MetadataManager(args.metadata_file)
    
    if args.action == 'update':
        # Crawl and update metadata
        print(f"Updating metadata for: {args.path}")
        
        crawler = FileCrawler(root_path=args.path)
        files = crawler.crawl()
        
        for rel_path, file_info in files.items():
            metadata_mgr.update_node(
                path=rel_path,
                sha256=file_info.sha256,
                last_modified=file_info.modified
            )
        
        metadata_mgr.save_metadata()
        print(f"Metadata updated for {len(files)} files")
        
    elif args.action == 'check':
        # Check for changes
        print(f"Checking for changes...")
        
        outdated = metadata_mgr.get_outdated_nodes()
        changed = metadata_mgr.get_changed_files(args.path)
        
        if not outdated and not changed:
            print("✓ All files are up to date")
        else:
            if outdated:
                print(f"\n⚠ Outdated files ({len(outdated)}):")
                for path in outdated[:10]:  # Show first 10
                    print(f"  - {path}")
                if len(outdated) > 10:
                    print(f"  ... and {len(outdated) - 10} more")
            
            if changed:
                print(f"\n⚠ Changed files ({len(changed)}):")
                for path, status in list(changed.items())[:10]:
                    print(f"  - {path}: {status}")
                if len(changed) > 10:
                    print(f"  ... and {len(changed) - 10} more")
        
    elif args.action == 'stats':
        # Show statistics
        stats = metadata_mgr.get_statistics()
        print("Metadata Statistics:")
        print(f"  Total nodes: {stats['total_nodes']}")
        print(f"  Up to date: {stats['up_to_date_nodes']}")
        print(f"  Outdated: {stats['outdated_nodes']}")
        print(f"  Dependencies: {stats['total_dependencies']}")
        print(f"  Last updated: {stats['last_updated']}")
    
    return 0


def cmd_query(args):
    """Query the codebase"""
    query_interface = CodebaseQueryInterface(args.path)
    
    if args.action == 'file':
        # Show file content
        content = query_interface.get_file_content(
            args.file,
            start_line=args.start_line,
            end_line=args.end_line
        )
        
        if content:
            print(content)
        else:
            print(f"Error: File '{args.file}' not found")
            return 1
    
    elif args.action == 'functions':
        # Extract functions
        functions = query_interface.extract_functions(args.file)
        
        if not functions:
            print(f"No functions found in '{args.file}'")
            return 0
        
        print(f"Functions in {args.file}:")
        for func in functions:
            print(f"\n{'='*60}")
            print(f"Function: {func.context}")
            print(f"Lines: {func.start_line}-{func.end_line}")
            print(f"{'='*60}")
            if args.verbose:
                print(func.content)
            else:
                # Show just signature
                first_line = func.content.split('\n')[0]
                print(first_line)
    
    elif args.action == 'classes':
        # Extract classes
        classes = query_interface.extract_classes(args.file)
        
        if not classes:
            print(f"No classes found in '{args.file}'")
            return 0
        
        print(f"Classes in {args.file}:")
        for cls in classes:
            print(f"\n{'='*60}")
            print(f"Class: {cls.context}")
            print(f"Lines: {cls.start_line}-{cls.end_line}")
            print(f"{'='*60}")
            if args.verbose:
                print(cls.content)
    
    elif args.action == 'summary':
        # Show file summary
        summary = query_interface.get_file_summary(args.file)
        
        if 'error' in summary:
            print(f"Error: {summary['error']}")
            return 1
        
        print(f"Summary of {args.file}:")
        print(f"  Lines: {summary['lines']}")
        print(f"  Size: {summary['size']} bytes")
        print(f"  Functions: {len(summary['functions'])}")
        if summary['functions']:
            for func in summary['functions']:
                print(f"    - {func}()")
        print(f"  Classes: {len(summary['classes'])}")
        if summary['classes']:
            for cls in summary['classes']:
                print(f"    - {cls}")
        print(f"  Imports: {len(summary['imports'])}")
        if args.verbose and summary['imports']:
            for imp in summary['imports']:
                print(f"    - {imp}")
    
    elif args.action == 'search':
        # Search for pattern
        snippets = query_interface.search_pattern(
            args.pattern,
            file_pattern=args.file_pattern,
            context_lines=args.context
        )
        
        if not snippets:
            print(f"No matches found for pattern: {args.pattern}")
            return 0
        
        print(f"Found {len(snippets)} matches:")
        for snippet in snippets[:args.max_results]:
            print(f"\n{'='*60}")
            print(f"File: {snippet.file_path}")
            print(f"Lines: {snippet.start_line}-{snippet.end_line}")
            print(f"{snippet.context}")
            print(f"{'='*60}")
            print(snippet.content)
    
    elif args.action == 'llm':
        # Format for LLM
        output = query_interface.format_for_llm(
            args.file,
            include_functions=not args.no_functions,
            include_classes=not args.no_classes
        )
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(output)
            print(f"LLM-formatted output saved to: {args.output}")
        else:
            print(output)
    
    return 0


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Jarvis Development Tools - CLI for codebase exploration',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # Crawl command
    crawl_parser = subparsers.add_parser('crawl', help='Crawl directory and collect file information')
    crawl_parser.add_argument('path', help='Directory to crawl')
    crawl_parser.add_argument('-o', '--output', help='Output JSON file')
    crawl_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    crawl_parser.add_argument('--max-size', type=int, default=10, help='Max file size in MB (default: 10)')
    
    # Metadata command
    metadata_parser = subparsers.add_parser('metadata', help='Manage metadata and check changes')
    metadata_parser.add_argument('action', choices=['update', 'check', 'stats'], help='Action to perform')
    metadata_parser.add_argument('-p', '--path', default='.', help='Path to check (default: current directory)')
    metadata_parser.add_argument('-m', '--metadata-file', default='.jarvis_metadata.json', 
                                  help='Metadata file path')
    
    # Query command
    query_parser = subparsers.add_parser('query', help='Query codebase information')
    query_parser.add_argument('action', choices=['file', 'functions', 'classes', 'summary', 'search', 'llm'],
                              help='Query action')
    query_parser.add_argument('-p', '--path', default='.', help='Root path (default: current directory)')
    query_parser.add_argument('-f', '--file', help='File to query')
    query_parser.add_argument('-s', '--start-line', type=int, help='Start line number')
    query_parser.add_argument('-e', '--end-line', type=int, help='End line number')
    query_parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    query_parser.add_argument('-o', '--output', help='Output file')
    query_parser.add_argument('--pattern', help='Search pattern (regex)')
    query_parser.add_argument('--file-pattern', default='*.py', help='File pattern for search')
    query_parser.add_argument('--context', type=int, default=3, help='Context lines for search')
    query_parser.add_argument('--max-results', type=int, default=20, help='Max search results')
    query_parser.add_argument('--no-functions', action='store_true', help='Exclude functions in LLM output')
    query_parser.add_argument('--no-classes', action='store_true', help='Exclude classes in LLM output')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 1
    
    try:
        if args.command == 'crawl':
            return cmd_crawl(args)
        elif args.command == 'metadata':
            return cmd_metadata(args)
        elif args.command == 'query':
            return cmd_query(args)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        return 130
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose if hasattr(args, 'verbose') else False:
            import traceback
            traceback.print_exc()
        return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
