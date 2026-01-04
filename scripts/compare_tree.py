#!/usr/bin/env python3
"""
Jarvis Development Tree Analyzer

This script analyzes the Jarvis implementation repository and compares it against
the desired file tree structure defined in JARVIS_FILE_TREE.md.

Features:
- Generates current file tree from implementation repo
- Compares against desired structure
- Tracks completion by priority level
- Generates comparison reports
- Identifies missing components
"""

import os
import json
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from collections import defaultdict


class FileTreeNode:
    """Represents a node in the file tree"""
    
    def __init__(self, name: str, path: str, priority: Optional[str] = None,
                 node_type: str = "file"):
        self.name = name
        self.path = path
        self.priority = priority  # P0, P1, P2, P3
        self.node_type = node_type  # file, directory, function
        self.children = []
        self.functions = []
        self.exists = False
        self.lines_of_code = 0
        
    def add_child(self, child):
        """Add a child node"""
        self.children.append(child)
        
    def add_function(self, function_name: str, priority: str):
        """Add a function to this file"""
        self.functions.append({
            'name': function_name,
            'priority': priority,
            'implemented': False
        })
        
    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            'name': self.name,
            'path': self.path,
            'priority': self.priority,
            'type': self.node_type,
            'exists': self.exists,
            'lines_of_code': self.lines_of_code,
            'functions': self.functions,
            'children': [child.to_dict() for child in self.children]
        }


class DesiredTreeParser:
    """Parse JARVIS_FILE_TREE.md to extract desired structure"""
    
    def __init__(self, tree_file_path: str):
        self.tree_file_path = tree_file_path
        self.root = FileTreeNode("jarvis", "jarvis", "P0", "directory")
        
    def parse(self) -> FileTreeNode:
        """Parse the file tree document"""
        with open(self.tree_file_path, 'r') as f:
            content = f.read()
        
        # Extract the tree structure from markdown code block
        tree_match = re.search(r'```\njarvis/\n(.*?)\n```', content, re.DOTALL)
        if not tree_match:
            raise ValueError("Could not find file tree structure in markdown")
        
        tree_content = tree_match.group(1)
        self._parse_tree_lines(tree_content.split('\n'))
        
        return self.root
    
    def _parse_tree_lines(self, lines: List[str]):
        """Parse individual lines of the tree"""
        # Configurable tree characters pattern
        TREE_CHARS = r'[│├└\s\t]'
        
        stack = [(0, self.root)]  # (indent_level, node)
        current_file = None
        
        for line in lines:
            if not line.strip():
                continue
            
            # Calculate indent level
            indent = len(line) - len(line.lstrip('│├└ \t'))
            indent_level = indent // 4
            
            # Extract file/directory name and priority with named groups
            match = re.search(
                r'(?P<tree_chars>' + TREE_CHARS + r'+)'
                r'(?P<name>[a-zA-Z0-9_\-./]+(?:\.[a-z]+)?)\s*'
                r'(?P<priority>\[P[0-3]\])?',
                line
            )
            if not match:
                # Check if this is a function line
                if '└── Functions:' in line or 'Functions:' in line:
                    continue
                # Function pattern with named groups
                func_match = re.search(
                    r'(?P<tree_chars>[├└│\s]+)'
                    r'(?P<func_name>[a-z_]+)\(\)\s*'
                    r'(?P<priority>\[P[0-3]\])',
                    line
                )
                if func_match and current_file:
                    func_name = func_match.group('func_name')
                    priority = func_match.group('priority').strip('[]')
                    current_file.add_function(func_name, priority)
                continue
            
            name = match.group('name').strip()
            priority = match.group('priority')
            if priority:
                priority = priority.strip('[]')
            
            # Determine if directory or file
            is_directory = name.endswith('/') or '.' not in name.split('/')[-1]
            node_type = "directory" if is_directory else "file"
            
            # Build full path
            parent = stack[-1][1] if stack else self.root
            while stack and stack[-1][0] >= indent_level:
                stack.pop()
            
            parent = stack[-1][1] if stack else self.root
            full_path = os.path.join(parent.path, name.rstrip('/'))
            
            node = FileTreeNode(name.rstrip('/'), full_path, priority, node_type)
            parent.add_child(node)
            
            if is_directory:
                stack.append((indent_level, node))
            else:
                current_file = node
    
    def extract_priority_stats(self) -> Dict[str, int]:
        """Extract statistics by priority level"""
        stats = defaultdict(int)
        
        def count_nodes(node: FileTreeNode):
            if node.priority:
                stats[node.priority] += 1
            for child in node.children:
                count_nodes(child)
        
        count_nodes(self.root)
        return dict(stats)


class ActualTreeScanner:
    """Scan actual Jarvis implementation repository"""
    
    # Default ignore patterns - can be overridden via constructor
    DEFAULT_IGNORE_PATTERNS = {
        '__pycache__', 'node_modules', 'venv', '.venv', 
        'env', '.env', '.git', '.pytest_cache', 
        'dist', 'build', '*.egg-info'
    }
    
    @staticmethod
    def build_ignore_patterns(base_patterns: set, additional: Optional[List[str]] = None) -> set:
        """Build ignore patterns set from base and additional patterns"""
        patterns = base_patterns.copy()
        if additional:
            patterns.update(additional)
        return patterns
    
    def __init__(self, repo_path: str, ignore_patterns: Optional[set] = None):
        self.repo_path = Path(repo_path)
        self.ignore_patterns = ignore_patterns or self.DEFAULT_IGNORE_PATTERNS
        
    def scan(self) -> FileTreeNode:
        """Scan the actual repository"""
        if not self.repo_path.exists():
            print(f"Warning: Repository path {self.repo_path} does not exist")
            return FileTreeNode("jarvis", str(self.repo_path), None, "directory")
        
        root = FileTreeNode("jarvis", str(self.repo_path), None, "directory")
        root.exists = True
        
        self._scan_directory(self.repo_path, root)
        return root
    
    def _scan_directory(self, path: Path, node: FileTreeNode):
        """Recursively scan directory"""
        try:
            for item in sorted(path.iterdir()):
                # Skip items matching ignore patterns
                if item.name.startswith('.') or item.name in self.ignore_patterns:
                    continue
                
                if item.is_dir():
                    child = FileTreeNode(item.name, str(item), None, "directory")
                    child.exists = True
                    node.add_child(child)
                    self._scan_directory(item, child)
                else:
                    child = FileTreeNode(item.name, str(item), None, "file")
                    child.exists = True
                    child.lines_of_code = self._count_lines(item)
                    
                    # Extract functions if Python file
                    if item.suffix == '.py':
                        child.functions = self._extract_functions(item)
                    
                    node.add_child(child)
        except PermissionError:
            pass
    
    def _count_lines(self, file_path: Path) -> int:
        """Count lines of code in file"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return len(f.readlines())
        except:
            return 0
    
    def _extract_functions(self, file_path: Path) -> List[Dict]:
        """Extract function definitions from Python file"""
        functions = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Find function definitions
            func_pattern = r'^\s*def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
            for match in re.finditer(func_pattern, content, re.MULTILINE):
                functions.append({
                    'name': match.group(1),
                    'priority': None,
                    'implemented': True
                })
        except:
            pass
        
        return functions


class TreeComparator:
    """Compare desired vs actual file trees"""
    
    def __init__(self, desired: FileTreeNode, actual: FileTreeNode):
        self.desired = desired
        self.actual = actual
        
    def compare(self) -> Dict:
        """Generate comprehensive comparison report"""
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': self._generate_summary(),
            'by_priority': self._compare_by_priority(),
            'missing_files': self._find_missing_files(),
            'extra_files': self._find_extra_files(),
            'function_coverage': self._compare_functions(),
            'recommendations': self._generate_recommendations()
        }
        
        return report
    
    def _generate_summary(self) -> Dict:
        """Generate overall summary statistics"""
        desired_count = self._count_nodes(self.desired)
        actual_count = self._count_nodes(self.actual)
        
        return {
            'desired_total_files': desired_count['files'],
            'desired_total_directories': desired_count['directories'],
            'actual_total_files': actual_count['files'],
            'actual_total_directories': actual_count['directories'],
            'completion_percentage': self._calculate_completion()
        }
    
    def _count_nodes(self, node: FileTreeNode, counts: Optional[Dict] = None) -> Dict:
        """Count nodes in tree"""
        if counts is None:
            counts = {'files': 0, 'directories': 0}
        
        if node.node_type == 'file':
            counts['files'] += 1
        elif node.node_type == 'directory':
            counts['directories'] += 1
        
        for child in node.children:
            self._count_nodes(child, counts)
        
        return counts
    
    def _calculate_completion(self) -> float:
        """Calculate overall completion percentage"""
        desired_files = self._get_all_files(self.desired)
        actual_paths = {f.path for f in self._get_all_files(self.actual)}
        
        if not desired_files:
            return 0.0
        
        matched = sum(1 for f in desired_files if any(f.name in path for path in actual_paths))
        return (matched / len(desired_files)) * 100
    
    def _compare_by_priority(self) -> Dict:
        """Compare files by priority level"""
        priorities = {}
        
        for priority in ['P0', 'P1', 'P2', 'P3']:
            desired_files = self._get_files_by_priority(self.desired, priority)
            actual_paths = {f.path for f in self._get_all_files(self.actual)}
            
            matched = sum(1 for f in desired_files if any(f.name in path for path in actual_paths))
            total = len(desired_files)
            
            priorities[priority] = {
                'total': total,
                'implemented': matched,
                'percentage': (matched / total * 100) if total > 0 else 0,
                'missing': total - matched
            }
        
        return priorities
    
    def _get_files_by_priority(self, node: FileTreeNode, priority: str) -> List[FileTreeNode]:
        """Get all files with specific priority"""
        files = []
        
        if node.node_type == 'file' and node.priority == priority:
            files.append(node)
        
        for child in node.children:
            files.extend(self._get_files_by_priority(child, priority))
        
        return files
    
    def _get_all_files(self, node: FileTreeNode) -> List[FileTreeNode]:
        """Get all files from tree"""
        files = []
        
        if node.node_type == 'file':
            files.append(node)
        
        for child in node.children:
            files.extend(self._get_all_files(child))
        
        return files
    
    def _find_missing_files(self) -> List[Dict]:
        """Find files in desired but not in actual"""
        desired_files = self._get_all_files(self.desired)
        actual_paths = {f.path for f in self._get_all_files(self.actual)}
        
        missing = []
        for desired_file in desired_files:
            if not any(desired_file.name in path for path in actual_paths):
                missing.append({
                    'path': desired_file.path,
                    'name': desired_file.name,
                    'priority': desired_file.priority
                })
        
        return sorted(missing, key=lambda x: (x['priority'] or 'P9', x['path']))
    
    def _find_extra_files(self) -> List[str]:
        """Find files in actual but not in desired"""
        desired_names = {f.name for f in self._get_all_files(self.desired)}
        actual_files = self._get_all_files(self.actual)
        
        extra = []
        for actual_file in actual_files:
            if actual_file.name not in desired_names:
                extra.append(actual_file.path)
        
        return sorted(extra)
    
    def _compare_functions(self) -> Dict:
        """Compare function implementations"""
        desired_files = self._get_all_files(self.desired)
        
        coverage = {
            'total_functions': 0,
            'implemented_functions': 0,
            'by_file': []
        }
        
        for desired_file in desired_files:
            if not desired_file.functions:
                continue
            
            total_funcs = len(desired_file.functions)
            coverage['total_functions'] += total_funcs
            
            # TODO: Match with actual implementation
            # For now, assume 0 implemented
            coverage['by_file'].append({
                'file': desired_file.path,
                'total': total_funcs,
                'implemented': 0,
                'percentage': 0
            })
        
        if coverage['total_functions'] > 0:
            coverage['overall_percentage'] = (coverage['implemented_functions'] / 
                                             coverage['total_functions'] * 100)
        else:
            coverage['overall_percentage'] = 0
        
        return coverage
    
    def _generate_recommendations(self) -> List[str]:
        """Generate recommendations based on comparison"""
        recommendations = []
        
        by_priority = self._compare_by_priority()
        
        # Check P0 completion
        if by_priority.get('P0', {}).get('percentage', 0) < 100:
            recommendations.append(
                f"CRITICAL: P0 (MVP) components are only {by_priority['P0']['percentage']:.1f}% complete. "
                f"Focus on completing {by_priority['P0']['missing']} remaining P0 files."
            )
        
        # Check if priorities are being followed
        if by_priority.get('P0', {}).get('percentage', 0) < 100:
            if by_priority.get('P1', {}).get('percentage', 0) > 0:
                recommendations.append(
                    "WARNING: P1 components started before P0 completion. "
                    "Consider focusing on P0 (MVP) first."
                )
        
        # Check overall progress
        summary = self._generate_summary()
        if summary['completion_percentage'] < 30:
            recommendations.append(
                f"Project is at {summary['completion_percentage']:.1f}% completion. "
                "Focus on core MVP components (P0) to reach first milestone."
            )
        
        return recommendations

def _generate_markdown_report(report: Dict) -> str:
    """Generate markdown version of report"""
    md = "# Jarvis File Tree Comparison Report\n\n"
    md += f"**Generated**: {report['timestamp']}\n\n"
    md += "---\n\n"
    
    # Summary
    md += "## Summary\n\n"
    summary = report['summary']
    md += f"- **Desired Files**: {summary['desired_total_files']}\n"
    md += f"- **Actual Files**: {summary['actual_total_files']}\n"
    md += f"- **Overall Completion**: {summary['completion_percentage']:.1f}%\n\n"
    
    # By Priority
    md += "## Completion by Priority\n\n"
    md += "| Priority | Total | Implemented | Missing | Percentage |\n"
    md += "|----------|-------|-------------|---------|------------|\n"
    
    for priority, stats in report['by_priority'].items():
        md += f"| {priority} | {stats['total']} | {stats['implemented']} | "
        md += f"{stats['missing']} | {stats['percentage']:.1f}% |\n"
    
    md += "\n"
    
    # Recommendations
    if report['recommendations']:
        md += "## Recommendations\n\n"
        for i, rec in enumerate(report['recommendations'], 1):
            md += f"{i}. {rec}\n"
        md += "\n"
    
    # Missing Files (top 20)
    if report['missing_files']:
        md += "## Missing Files (Top 20 by Priority)\n\n"
        for missing in report['missing_files'][:20]:
            md += f"- `{missing['path']}` [{missing['priority']}]\n"
        md += "\n"
    
    return md


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Compare Jarvis desired vs actual file tree'
    )
    parser.add_argument(
        '--desired',
        default='JARVIS_FILE_TREE.md',
        help='Path to desired tree markdown file'
    )
    parser.add_argument(
        '--actual',
        default='../jarvis',
        help='Path to actual Jarvis implementation repository'
    )
    parser.add_argument(
        '--output',
        default='tracking/reports',
        help='Output directory for reports'
    )
    parser.add_argument(
        '--ignore',
        nargs='*',
        help='Additional patterns to ignore when scanning (e.g., "*.pyc" "temp/")'
    )
    
    args = parser.parse_args()
    
    # Ensure output directory exists
    os.makedirs(args.output, exist_ok=True)
    
    # Build ignore patterns using helper
    ignore_patterns = ActualTreeScanner.build_ignore_patterns(
        ActualTreeScanner.DEFAULT_IGNORE_PATTERNS,
        args.ignore
    )
    
    # Generate report with custom ignore patterns
    print("Parsing desired file tree...")
    parser = DesiredTreeParser(args.desired)
    desired_tree = parser.parse()
    
    print("Scanning actual repository...")
    scanner = ActualTreeScanner(args.actual, ignore_patterns)
    actual_tree = scanner.scan()
    
    print("Comparing trees...")
    comparator = TreeComparator(desired_tree, actual_tree)
    report = comparator.compare()
    
    print("Generating report...")
    # Save JSON report
    json_output = os.path.join(args.output, 'tree_comparison.json')
    with open(json_output, 'w') as f:
        json.dump(report, f, indent=2)
    
    # Generate Markdown report
    md_output = os.path.join(args.output, 'tree_comparison.md')
    with open(md_output, 'w') as f:
        f.write(_generate_markdown_report(report))
    
    print(f"Reports generated:")
    print(f"  - JSON: {json_output}")
    print(f"  - Markdown: {md_output}")
    
    # Print summary
    print("\n" + "="*50)
    print("COMPARISON SUMMARY")
    print("="*50)
    print(f"Overall Completion: {report['summary']['completion_percentage']:.1f}%")
    print("\nBy Priority:")
    for priority, stats in report['by_priority'].items():
        print(f"  {priority}: {stats['percentage']:.1f}% "
              f"({stats['implemented']}/{stats['total']})")
    print("\nSee generated reports for full details.")
