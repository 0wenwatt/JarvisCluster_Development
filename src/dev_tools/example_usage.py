#!/usr/bin/env python3
"""
Example Usage of Jarvis Development Tools

This script demonstrates how to use the dev_tools package for:
1. Crawling a codebase and collecting metadata
2. Tracking changes with SHA256 hashing
3. Querying files and extracting code snippets
4. Formatting output for LLM consumption
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from crawler import FileCrawler
from metadata_manager import MetadataManager
from query_interface import CodebaseQueryInterface


def example_1_crawl_codebase():
    """Example 1: Crawl a directory and collect file information"""
    print("=" * 70)
    print("EXAMPLE 1: Crawling Codebase")
    print("=" * 70)
    
    # Create crawler for the dev_tools directory itself
    crawler = FileCrawler(
        root_path=".",
        include_extensions=['.py', '.md']  # Only Python and Markdown files
    )
    
    # Crawl with progress callback
    print("\nCrawling directory...")
    
    def progress(file_path):
        print(f"  Found: {file_path}")
    
    files = crawler.crawl(update_callback=progress)
    
    # Show statistics
    stats = crawler.get_statistics()
    print(f"\n✓ Crawl complete!")
    print(f"  Total files: {stats['total_files']}")
    print(f"  Total lines: {stats['total_lines']:,}")
    print(f"  Total size: {stats['total_size']:,} bytes")
    
    # Show breakdown by extension
    print("\n  Files by extension:")
    for ext, count in stats['extensions'].items():
        print(f"    {ext}: {count} files")
    
    return files


def example_2_metadata_tracking():
    """Example 2: Track file metadata and changes"""
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Metadata Tracking and Change Detection")
    print("=" * 70)
    
    # Create metadata manager
    metadata = MetadataManager(metadata_file="/tmp/example_metadata.json")
    
    # Crawl and update metadata
    print("\nUpdating metadata...")
    crawler = FileCrawler(root_path=".")
    files = crawler.crawl()
    
    for rel_path, file_info in files.items():
        metadata.update_node(
            path=rel_path,
            sha256=file_info.sha256,
            last_modified=file_info.modified
        )
    
    # Save metadata
    metadata.save_metadata()
    
    # Show statistics
    stats = metadata.get_statistics()
    print(f"\n✓ Metadata updated!")
    print(f"  Total nodes tracked: {stats['total_nodes']}")
    print(f"  Up to date: {stats['up_to_date_nodes']}")
    print(f"  Outdated: {stats['outdated_nodes']}")
    
    # Check for changes
    print("\nChecking for changes...")
    changed = metadata.get_changed_files()
    if changed:
        print(f"  Found {len(changed)} changed files:")
        for path, status in list(changed.items())[:5]:
            print(f"    - {path}: {status}")
    else:
        print("  No changes detected")
    
    return metadata


def example_3_query_files():
    """Example 3: Query files and extract information"""
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Querying Files and Extracting Code")
    print("=" * 70)
    
    # Create query interface
    query = CodebaseQueryInterface(root_path=".")
    
    # Example file to query
    example_file = "crawler.py"
    
    print(f"\nQuerying file: {example_file}")
    
    # Get file summary
    print("\n--- File Summary ---")
    summary = query.get_file_summary(example_file)
    if 'error' not in summary:
        print(f"  Lines: {summary['lines']}")
        print(f"  Size: {summary['size']} bytes")
        print(f"  Functions: {len(summary['functions'])}")
        print(f"  Classes: {len(summary['classes'])}")
        print(f"  Imports: {len(summary['imports'])}")
        
        # Show function names
        if summary['functions']:
            print("\n  Functions found:")
            for func in summary['functions'][:5]:  # First 5
                print(f"    - {func}()")
        
        # Show class names
        if summary['classes']:
            print("\n  Classes found:")
            for cls in summary['classes']:
                print(f"    - {cls}")
    
    # Extract specific functions
    print("\n--- Extracting Functions ---")
    functions = query.extract_functions(example_file)
    if functions:
        print(f"  Found {len(functions)} functions")
        # Show first function
        func = functions[0]
        print(f"\n  First function: {func.context}")
        print(f"  Lines: {func.start_line}-{func.end_line}")
        print(f"  Preview:")
        lines = func.content.split('\n')[:3]
        for line in lines:
            print(f"    {line}")
    
    return query


def example_4_llm_formatting():
    """Example 4: Format code for LLM consumption"""
    print("\n" + "=" * 70)
    print("EXAMPLE 4: LLM-Optimized Formatting")
    print("=" * 70)
    
    query = CodebaseQueryInterface(root_path=".")
    
    # Format a file for LLM
    example_file = "crawler.py"
    print(f"\nFormatting {example_file} for LLM consumption...")
    
    llm_output = query.format_for_llm(
        example_file,
        include_functions=True,
        include_classes=True,
        max_content_length=2000  # Limit for demo
    )
    
    # Show preview (first 1000 chars)
    print("\n--- LLM Output Preview (first 1000 chars) ---")
    print(llm_output[:1000])
    print("\n... (truncated for display)")
    
    # Save to file
    output_file = "/tmp/llm_formatted.txt"
    with open(output_file, 'w') as f:
        f.write(llm_output)
    
    print(f"\n✓ Full output saved to: {output_file}")
    
    return llm_output


def example_5_search_patterns():
    """Example 5: Search for patterns in the codebase"""
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Pattern Search")
    print("=" * 70)
    
    query = CodebaseQueryInterface(root_path=".")
    
    # Search for class definitions
    print("\nSearching for class definitions...")
    snippets = query.search_pattern(
        pattern=r"^class\s+\w+",
        file_pattern="*.py",
        context_lines=2
    )
    
    print(f"  Found {len(snippets)} matches")
    
    # Show first match
    if snippets:
        snippet = snippets[0]
        print(f"\n  First match:")
        print(f"    File: {snippet.file_path}")
        print(f"    Lines: {snippet.start_line}-{snippet.end_line}")
        print(f"    Context: {snippet.context}")
        print(f"\n    Content preview:")
        lines = snippet.content.split('\n')[:5]
        for line in lines:
            print(f"      {line}")
    
    return snippets


def example_6_dependency_tracking():
    """Example 6: Track dependencies between files"""
    print("\n" + "=" * 70)
    print("EXAMPLE 6: Dependency Tracking")
    print("=" * 70)
    
    metadata = MetadataManager(metadata_file="/tmp/example_metadata.json")
    
    # Add a sample dependency
    print("\nAdding dependency example...")
    print("  cli.py depends on crawler.py")
    
    # Get actual file hashes
    crawler = FileCrawler(root_path=".")
    files = crawler.crawl()
    
    if 'cli.py' in files and 'crawler.py' in files:
        cli_info = files['cli.py']
        crawler_info = files['crawler.py']
        
        # Update node metadata
        metadata.update_node(
            path='cli.py',
            sha256=cli_info.sha256,
            last_modified=cli_info.modified,
            dependencies=['crawler.py', 'metadata_manager.py', 'query_interface.py']
        )
        
        # Add dependency
        metadata.add_dependency(
            node_path='cli.py',
            dependency_path='crawler.py',
            dependency_sha256=crawler_info.sha256,
            dependency_modified=crawler_info.modified
        )
        
        metadata.save_metadata()
        
        print("\n✓ Dependencies added!")
        
        # Get dependency chain
        chain = metadata.get_dependency_chain('cli.py')
        print(f"\n  Dependency chain for cli.py:")
        for dep in chain:
            print(f"    - {dep}")
        
        # Check if up to date
        is_current = metadata.is_up_to_date('cli.py')
        status = "✓ up to date" if is_current else "⚠ outdated"
        print(f"\n  Status: {status}")


def main():
    """Run all examples"""
    print("\n")
    print("*" * 70)
    print("*" + " " * 68 + "*")
    print("*" + "  Jarvis Development Tools - Example Usage".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*" * 70)
    print("\nThis script demonstrates the key features of the dev_tools package.")
    print("Press Enter to continue through the examples...")
    input()
    
    try:
        # Run examples
        example_1_crawl_codebase()
        input("\nPress Enter to continue...")
        
        example_2_metadata_tracking()
        input("\nPress Enter to continue...")
        
        example_3_query_files()
        input("\nPress Enter to continue...")
        
        example_4_llm_formatting()
        input("\nPress Enter to continue...")
        
        example_5_search_patterns()
        input("\nPress Enter to continue...")
        
        example_6_dependency_tracking()
        
        print("\n" + "=" * 70)
        print("All examples completed successfully!")
        print("=" * 70)
        print("\nNext steps:")
        print("  1. Try the CLI: python3 cli.py --help")
        print("  2. Read the README.md for more details")
        print("  3. Use the tools in your own development workflow")
        print("\n")
        
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        return 1
    except Exception as e:
        print(f"\n\nError: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
