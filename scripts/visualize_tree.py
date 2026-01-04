#!/usr/bin/env python3
"""
Generate Visual File Tree

Creates a visual representation of the Jarvis file tree with:
- Color coding by priority
- Development order indicators
- Completion status markers
- Interactive HTML visualization
"""

import json
from pathlib import Path
from typing import Dict, List


def generate_ascii_tree(tree_data: Dict, output_file: str = None):
    """
    Generate ASCII art representation of file tree
    
    Args:
        tree_data: Parsed tree structure
        output_file: Optional file to write output
    """
    lines = []
    
    def add_node(node: Dict, prefix: str = "", is_last: bool = True):
        """Recursively add nodes to output"""
        # Choose connector
        connector = "└── " if is_last else "├── "
        
        # Get priority indicator
        priority = node.get('priority', '')
        priority_str = f" [{priority}]" if priority else ""
        
        # Get existence marker
        exists = node.get('exists', False)
        marker = "✓" if exists else "✗"
        
        # Add line
        name = node.get('name', '')
        lines.append(f"{prefix}{connector}{marker} {name}{priority_str}")
        
        # Prepare prefix for children
        if is_last:
            child_prefix = prefix + "    "
        else:
            child_prefix = prefix + "│   "
        
        # Process children
        children = node.get('children', [])
        for i, child in enumerate(children):
            is_last_child = (i == len(children) - 1)
            add_node(child, child_prefix, is_last_child)
    
    # Start with root
    lines.append(tree_data.get('name', 'root'))
    for i, child in enumerate(tree_data.get('children', [])):
        is_last = (i == len(tree_data['children']) - 1)
        add_node(child, "", is_last)
    
    output = "\n".join(lines)
    
    if output_file:
        with open(output_file, 'w') as f:
            f.write(output)
    
    return output


def generate_html_tree(tree_data: Dict, output_file: str):
    """
    Generate interactive HTML visualization
    
    Features:
    - Collapsible tree structure
    - Color-coded priorities
    - Filter by priority
    - Search functionality
    """
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jarvis File Tree Visualization</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            padding: 20px;
            background: #1e1e1e;
            color: #d4d4d4;
        }
        
        .header {
            background: #252526;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
        }
        
        h1 {
            color: #4ec9b0;
            margin-bottom: 10px;
        }
        
        .controls {
            margin-top: 15px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        
        .filter-btn {
            padding: 8px 16px;
            background: #3c3c3c;
            border: 1px solid #555;
            color: #d4d4d4;
            cursor: pointer;
            border-radius: 4px;
            transition: all 0.2s;
        }
        
        .filter-btn:hover {
            background: #555;
        }
        
        .filter-btn.active {
            background: #007acc;
            border-color: #007acc;
        }
        
        .search-box {
            padding: 8px;
            background: #3c3c3c;
            border: 1px solid #555;
            color: #d4d4d4;
            border-radius: 4px;
            width: 300px;
        }
        
        .tree {
            background: #252526;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
        }
        
        .tree-node {
            margin-left: 20px;
            padding: 2px 0;
        }
        
        .tree-node.root {
            margin-left: 0;
        }
        
        .node-content {
            cursor: pointer;
            padding: 2px 4px;
            border-radius: 3px;
        }
        
        .node-content:hover {
            background: #2d2d30;
        }
        
        .node-name {
            color: #9cdcfe;
        }
        
        .directory .node-name {
            color: #dcdcaa;
            font-weight: bold;
        }
        
        .priority {
            color: #888;
            font-size: 0.9em;
            margin-left: 8px;
        }
        
        .priority.P0 { color: #f44336; font-weight: bold; }
        .priority.P1 { color: #ff9800; }
        .priority.P2 { color: #4caf50; }
        .priority.P3 { color: #2196f3; }
        
        .status {
            margin-left: 8px;
            font-size: 0.9em;
        }
        
        .status.exists { color: #4caf50; }
        .status.missing { color: #f44336; }
        
        .functions {
            margin-left: 30px;
            font-size: 0.9em;
            color: #808080;
        }
        
        .function-item {
            padding: 2px 0;
        }
        
        .toggle {
            display: inline-block;
            width: 16px;
            text-align: center;
            cursor: pointer;
            user-select: none;
        }
        
        .collapsed > .tree-node {
            display: none;
        }
        
        .hidden {
            display: none !important;
        }
        
        .stats {
            background: #252526;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 8px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
        }
        
        .stat-card {
            background: #2d2d30;
            padding: 15px;
            border-radius: 6px;
            border-left: 4px solid #007acc;
        }
        
        .stat-label {
            color: #888;
            font-size: 0.9em;
            margin-bottom: 5px;
        }
        
        .stat-value {
            font-size: 1.5em;
            color: #4ec9b0;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🌳 Jarvis File Tree Visualization</h1>
        <p>Interactive view of the Jarvis implementation structure with development priorities</p>
        
        <div class="controls">
            <button class="filter-btn active" data-filter="all">All</button>
            <button class="filter-btn" data-filter="P0">P0 (MVP)</button>
            <button class="filter-btn" data-filter="P1">P1 (Core)</button>
            <button class="filter-btn" data-filter="P2">P2 (Advanced)</button>
            <button class="filter-btn" data-filter="P3">P3 (Future)</button>
            <button class="filter-btn" data-filter="exists">Implemented Only</button>
            <button class="filter-btn" data-filter="missing">Missing Only</button>
            <input type="text" class="search-box" placeholder="Search files..." id="searchBox">
        </div>
    </div>
    
    <div class="stats" id="stats">
        <!-- Stats will be injected here -->
    </div>
    
    <div class="tree" id="tree">
        <!-- Tree will be injected here -->
    </div>
    
    <script>
        const treeData = """ + json.dumps(tree_data, ensure_ascii=True) + """;
        
        // Calculate statistics
        function calculateStats(node, stats = { total: 0, p0: 0, p1: 0, p2: 0, p3: 0, exists: 0 }) {
            if (node.type === 'file') {
                stats.total++;
                if (node.priority) {
                    stats[node.priority.toLowerCase()]++;
                }
                if (node.exists) {
                    stats.exists++;
                }
            }
            
            if (node.children) {
                node.children.forEach(child => calculateStats(child, stats));
            }
            
            return stats;
        }
        
        // Render statistics
        function renderStats() {
            const stats = calculateStats(treeData);
            const completion = stats.total > 0 ? ((stats.exists / stats.total) * 100).toFixed(1) : 0;
            
            document.getElementById('stats').innerHTML = `
                <div class="stat-card">
                    <div class="stat-label">Total Files</div>
                    <div class="stat-value">${stats.total}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Implemented</div>
                    <div class="stat-value">${stats.exists}</div>
                </div>
                <div class="stat-card">
                    <div class="stat-label">Completion</div>
                    <div class="stat-value">${completion}%</div>
                </div>
                <div class="stat-card" style="border-left-color: #f44336;">
                    <div class="stat-label">P0 (MVP)</div>
                    <div class="stat-value">${stats.p0}</div>
                </div>
                <div class="stat-card" style="border-left-color: #ff9800;">
                    <div class="stat-label">P1 (Core)</div>
                    <div class="stat-value">${stats.p1}</div>
                </div>
                <div class="stat-card" style="border-left-color: #4caf50;">
                    <div class="stat-label">P2 (Advanced)</div>
                    <div class="stat-value">${stats.p2}</div>
                </div>
            `;
        }
        
        // Render tree node
        function renderNode(node, isRoot = false) {
            const isDir = node.type === 'directory';
            const hasChildren = node.children && node.children.length > 0;
            const hasFunctions = node.functions && node.functions.length > 0;
            
            let html = '<div class="tree-node' + (isRoot ? ' root' : '') + '" ';
            html += `data-priority="${node.priority || 'none'}" `;
            html += `data-exists="${node.exists ? 'true' : 'false'}" `;
            html += `data-name="${node.name.toLowerCase()}"`;
            html += '>';
            
            html += '<div class="node-content ' + (isDir ? 'directory' : 'file') + '">';
            
            if (hasChildren) {
                html += '<span class="toggle" onclick="toggleNode(this)">▼</span>';
            } else {
                html += '<span class="toggle"></span>';
            }
            
            html += '<span class="node-name">';
            html += isDir ? '📁 ' : '📄 ';
            html += node.name;
            html += '</span>';
            
            if (node.priority) {
                html += `<span class="priority ${node.priority}">${node.priority}</span>`;
            }
            
            if (node.type === 'file') {
                html += `<span class="status ${node.exists ? 'exists' : 'missing'}">`;
                html += node.exists ? '✓' : '✗';
                html += '</span>';
            }
            
            html += '</div>';
            
            // Render functions
            if (hasFunctions) {
                html += '<div class="functions">';
                node.functions.forEach(func => {
                    html += '<div class="function-item">';
                    html += `<span>${func.name}()</span>`;
                    if (func.priority) {
                        html += `<span class="priority ${func.priority}">${func.priority}</span>`;
                    }
                    html += `<span class="status ${func.implemented ? 'exists' : 'missing'}">`;
                    html += func.implemented ? '✓' : '✗';
                    html += '</span>';
                    html += '</div>';
                });
                html += '</div>';
            }
            
            // Render children
            if (hasChildren) {
                node.children.forEach(child => {
                    html += renderNode(child);
                });
            }
            
            html += '</div>';
            return html;
        }
        
        // Toggle node expansion
        function toggleNode(element) {
            const node = element.closest('.tree-node');
            node.classList.toggle('collapsed');
            element.textContent = node.classList.contains('collapsed') ? '▶' : '▼';
        }
        
        // Filter tree
        function filterTree(filterType) {
            const nodes = document.querySelectorAll('.tree-node');
            
            nodes.forEach(node => {
                let show = true;
                
                if (filterType !== 'all') {
                    const priority = node.getAttribute('data-priority');
                    const exists = node.getAttribute('data-exists') === 'true';
                    
                    if (filterType === 'exists') {
                        show = exists;
                    } else if (filterType === 'missing') {
                        show = !exists && priority !== 'none';
                    } else {
                        show = priority === filterType;
                    }
                }
                
                node.classList.toggle('hidden', !show);
            });
        }
        
        // Search tree
        function searchTree(query) {
            query = query.toLowerCase();
            const nodes = document.querySelectorAll('.tree-node');
            
            if (!query) {
                nodes.forEach(node => node.classList.remove('hidden'));
                return;
            }
            
            nodes.forEach(node => {
                const name = node.getAttribute('data-name');
                const matches = name.includes(query);
                node.classList.toggle('hidden', !matches);
            });
        }
        
        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            renderStats();
            document.getElementById('tree').innerHTML = renderNode(treeData, true);
            
            // Filter buttons
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                    e.target.classList.add('active');
                    filterTree(e.target.getAttribute('data-filter'));
                });
            });
            
            // Search
            document.getElementById('searchBox').addEventListener('input', (e) => {
                searchTree(e.target.value);
            });
        });
    </script>
</body>
</html>
    """
    
    with open(output_file, 'w') as f:
        f.write(html)


if __name__ == '__main__':
    import argparse
    import sys
    
    parser = argparse.ArgumentParser(description='Generate visual file tree')
    parser.add_argument('--input', default='tracking/reports/tree_comparison.json',
                       help='Input JSON file from tree comparison')
    parser.add_argument('--output-ascii', default='tracking/reports/tree_visual.txt',
                       help='Output ASCII tree file')
    parser.add_argument('--output-html', default='tracking/reports/tree_visual.html',
                       help='Output HTML visualization')
    
    args = parser.parse_args()
    
    # Load tree data from comparison output
    try:
        with open(args.input, 'r') as f:
            comparison_data = json.load(f)
        
        # Extract tree structure from comparison data
        # The comparison data contains desired tree structure
        # For now, create a simple representation
        # In production, you'd parse the comparison output to build the tree
        
        print("Note: Full tree parsing from comparison data not yet implemented.")
        print("Generating sample visualization structure...")
        
        # Create a sample tree structure for demonstration
        sample_tree = {
            'name': 'jarvis',
            'type': 'directory',
            'priority': None,
            'exists': False,
            'children': [
                {
                    'name': 'api',
                    'type': 'directory',
                    'priority': 'P0',
                    'exists': True,
                    'children': [
                        {'name': 'server.py', 'type': 'file', 'priority': 'P0', 'exists': True, 'functions': []},
                        {'name': 'routes', 'type': 'directory', 'priority': 'P0', 'exists': False, 'children': []}
                    ]
                },
                {
                    'name': 'scheduler',
                    'type': 'directory',
                    'priority': 'P0',
                    'exists': False,
                    'children': []
                }
            ]
        }
        
        print("Generating ASCII tree...")
        ascii_tree = generate_ascii_tree(sample_tree, args.output_ascii)
        print(f"ASCII tree saved to: {args.output_ascii}")
        
        print("Generating HTML visualization...")
        generate_html_tree(sample_tree, args.output_html)
        print(f"HTML visualization saved to: {args.output_html}")
        print(f"Open {args.output_html} in a browser to view the interactive tree.")
        
    except FileNotFoundError:
        print(f"Error: Input file {args.input} not found.", file=sys.stderr)
        print("Please run compare_tree.py first to generate the comparison data.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {args.input}: {e}", file=sys.stderr)
        sys.exit(1)
