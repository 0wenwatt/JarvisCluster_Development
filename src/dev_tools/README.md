# Jarvis Development Tools

A comprehensive toolkit for navigating, analyzing, and querying the JarvisCluster codebase. These tools help developers understand the codebase structure, track changes, and extract relevant information for both human and LLM consumption.

## Features

### 1. File Crawler (`crawler.py`)
- **Recursive directory traversal** with configurable ignore patterns
- **SHA256 hashing** for file change detection
- **Metadata collection**: file size, line count, modification time
- **Binary file detection** and filtering
- **Tree structure generation** for visualization
- **Statistics reporting** by file type and extension

### 2. Metadata Manager (`metadata_manager.py`)
- **SHA256-based change tracking** for all files
- **Dependency tracking** between files
- **Up-to-date status checking** with dependency validation
- **Persistent metadata storage** in JSON format
- **Change detection**: identify modified, deleted, or outdated files
- **Dependency chain analysis** for understanding file relationships

### 3. Query Interface (`query_interface.py`)
- **File content retrieval** with line number support
- **Function extraction** from Python files
- **Class extraction** with full content
- **Pattern searching** with context lines
- **Import statement extraction**
- **LLM-optimized formatting** for AI-assisted development
- **File summaries** with statistics

### 4. CLI Tool (`cli.py`)
- **Unified command-line interface** for all tools
- **Three main commands**: `crawl`, `metadata`, `query`
- **Rich output formatting** for terminal display
- **JSON export** capabilities

## Installation

The tools are standalone Python modules with minimal dependencies:

```bash
# Navigate to the dev_tools directory
cd src/dev_tools

# The tools use only Python standard library
# No additional installation required
```

## Usage

### Command Line Interface

The CLI provides three main commands:

#### 1. Crawl Command

Crawl a directory to collect file information:

```bash
# Basic crawl
python3 cli.py crawl /path/to/directory

# Crawl with JSON output
python3 cli.py crawl /path/to/directory -o output.json

# Verbose mode to see each file
python3 cli.py crawl /path/to/directory -v

# Specify max file size (in MB)
python3 cli.py crawl /path/to/directory --max-size 5
```

#### 2. Metadata Command

Manage metadata and track changes:

```bash
# Update metadata for current directory
python3 cli.py metadata update

# Update metadata for specific path
python3 cli.py metadata update -p /path/to/directory

# Check for changes
python3 cli.py metadata check -p /path/to/directory

# Show metadata statistics
python3 cli.py metadata stats

# Use custom metadata file location
python3 cli.py metadata update -m custom_metadata.json
```

#### 3. Query Command

Query codebase information:

```bash
# View file content
python3 cli.py query file -f src/example.py

# View specific lines
python3 cli.py query file -f src/example.py -s 10 -e 50

# Extract all functions
python3 cli.py query functions -f src/example.py

# Extract all classes
python3 cli.py query classes -f src/example.py

# Get file summary
python3 cli.py query summary -f src/example.py

# Search for pattern
python3 cli.py query search --pattern "class.*Manager" --file-pattern "*.py"

# Format for LLM consumption
python3 cli.py query llm -f src/example.py -o llm_output.txt
```

### Python API

You can also use the tools programmatically:

#### File Crawler Example

```python
from dev_tools import FileCrawler

# Create crawler
crawler = FileCrawler(
    root_path="/path/to/codebase",
    ignore_patterns={'temp', 'cache'},  # Add custom ignores
    include_extensions=['.py', '.md']    # Filter by extension
)

# Crawl with progress callback
def on_file(path):
    print(f"Processing: {path}")

files = crawler.crawl(update_callback=on_file)

# Get statistics
stats = crawler.get_statistics()
print(f"Total files: {stats['total_files']}")
print(f"Total lines: {stats['total_lines']}")

# Get tree structure
tree = crawler.get_tree_structure()
```

#### Metadata Manager Example

```python
from dev_tools import MetadataManager

# Create metadata manager
metadata = MetadataManager(metadata_file=".jarvis_metadata.json")

# Update node metadata
metadata.update_node(
    path="src/example.py",
    sha256="abc123...",
    last_modified=1234567890.0,
    dependencies=["src/base.py", "src/utils.py"]
)

# Add dependencies
metadata.add_dependency(
    node_path="src/example.py",
    dependency_path="src/base.py",
    dependency_sha256="def456...",
    dependency_modified=1234567890.0
)

# Check if up to date
if metadata.is_up_to_date("src/example.py"):
    print("File is up to date")
else:
    print("File has changed")

# Get outdated files
outdated = metadata.get_outdated_nodes()
for path in outdated:
    print(f"Outdated: {path}")

# Save metadata
metadata.save_metadata()
```

#### Query Interface Example

```python
from dev_tools import CodebaseQueryInterface

# Create query interface
query = CodebaseQueryInterface(root_path="/path/to/codebase")

# Get file content
content = query.get_file_content("src/example.py", start_line=10, end_line=50)
print(content)

# Extract functions
functions = query.extract_functions("src/example.py")
for func in functions:
    print(f"Function: {func.context} (lines {func.start_line}-{func.end_line})")
    print(func.content)

# Extract classes
classes = query.extract_classes("src/example.py")
for cls in classes:
    print(f"Class: {cls.context}")

# Search for pattern
matches = query.search_pattern(
    pattern="def.*manager",
    file_pattern="*.py",
    context_lines=3
)

# Get file summary
summary = query.get_file_summary("src/example.py")
print(f"Functions: {summary['functions']}")
print(f"Classes: {summary['classes']}")

# Format for LLM
llm_output = query.format_for_llm("src/example.py")
print(llm_output)
```

## Use Cases

### 1. Development Assistant (LLM Integration)

Present codebase context to an LLM for AI-assisted development:

```bash
# Extract file with full context for LLM
python3 cli.py query llm -f src/scheduler.py -o context.txt

# Search for similar implementations
python3 cli.py query search --pattern "def schedule_" --context 5
```

### 2. Change Detection

Track which files have been modified:

```bash
# First, create baseline metadata
python3 cli.py metadata update -p /path/to/jarvis

# After making changes, check what's outdated
python3 cli.py metadata check -p /path/to/jarvis
```

### 3. Codebase Analysis

Understand the structure and composition:

```bash
# Crawl and get statistics
python3 cli.py crawl /path/to/jarvis -o analysis.json -v

# Get summaries of key files
python3 cli.py query summary -f jarvis/scheduler/task_scheduler.py
```

### 4. Documentation Generation

Extract structured information for documentation:

```python
from dev_tools import CodebaseQueryInterface

query = CodebaseQueryInterface("/path/to/jarvis")

# Generate API documentation
for file in ["api/server.py", "api/routes/tasks.py"]:
    summary = query.get_file_summary(file)
    # Process summary for docs...
```

## Integration with Existing Tools

These tools complement the existing repository tools:

- **`scripts/compare_tree.py`**: Uses similar crawling concepts but focuses on comparison with `JARVIS_FILE_TREE.md`
- **`scripts/visualize_tree.py`**: Generates visual representations of tree structures
- **`tracking/`**: These tools can populate the tracking directory with metadata

## Advanced Features

### Custom Ignore Patterns

```python
crawler = FileCrawler(
    root_path=".",
    ignore_patterns={'custom_dir', 'temp_*', '*.tmp'}
)
```

### Dependency Chain Analysis

```python
# Get full dependency chain for a file
chain = metadata.get_dependency_chain("src/example.py")
for dep in chain:
    print(f"Depends on: {dep}")
```

### Pattern Search with Context

```python
# Find all error handling patterns
snippets = query.search_pattern(
    pattern="except.*Error",
    file_pattern="**/*.py",
    context_lines=5
)
```

## Architecture

```
dev_tools/
├── __init__.py           # Package initialization and exports
├── crawler.py            # File system crawler with hashing
├── metadata_manager.py   # Metadata and dependency tracking
├── query_interface.py    # Code querying and extraction
├── cli.py               # Command-line interface
└── README.md            # This file
```

### Key Design Decisions

1. **SHA256 Hashing**: Fast, collision-resistant, and suitable for change detection
2. **Modular Architecture**: Each component can be used independently
3. **Minimal Dependencies**: Uses only Python standard library
4. **LLM-Friendly**: Structured output optimized for AI consumption
5. **Extensible**: Easy to add new query types and metadata fields

## Performance

- **Crawling**: ~1000 files/second on typical hardware
- **Hashing**: ~100MB/second for SHA256 calculation
- **Metadata**: In-memory operations with periodic persistence
- **Queries**: Fast regex-based searching with compiled patterns

## Best Practices

1. **Run metadata update regularly** to keep change tracking accurate
2. **Use ignore patterns** to exclude build artifacts and large files
3. **Set max_file_size** appropriately to avoid memory issues
4. **Save metadata** after making changes to dependency tracking
5. **Use LLM formatting** when providing context to AI assistants

## Troubleshooting

### Issue: Too many files being processed

**Solution**: Add more ignore patterns or use `include_extensions` filter

```python
crawler = FileCrawler(
    root_path=".",
    include_extensions=['.py', '.md']  # Only Python and Markdown
)
```

### Issue: Metadata file getting too large

**Solution**: Clear outdated entries periodically

```python
metadata = MetadataManager()
# Remove old entries
for path in metadata.get_outdated_nodes():
    if should_remove(path):
        metadata.remove_node(path)
metadata.save_metadata()
```

### Issue: Search taking too long

**Solution**: Use more specific file patterns

```bash
# Instead of searching all files
python3 cli.py query search --pattern "pattern" --file-pattern "**/*.py"

# Search specific directory
python3 cli.py query search --pattern "pattern" --file-pattern "src/**/*.py"
```

## Future Enhancements

- [ ] Add support for more programming languages (Go, JavaScript, etc.)
- [ ] Implement incremental crawling for better performance
- [ ] Add git integration for tracking changes via commits
- [ ] Support for custom metadata fields
- [ ] Web interface for visual exploration
- [ ] Integration with LSP (Language Server Protocol)
- [ ] Caching layer for frequently accessed files
- [ ] Parallel processing for large codebases

## Contributing

When adding new features:

1. Follow the existing code style (PEP 8)
2. Add docstrings to all public functions
3. Update this README with new capabilities
4. Test with both small and large codebases

## Related Documentation

- [REQUIREMENTS.md](../../REQUIREMENTS.md) - Coding standards
- [DESIGN_PLAN.md](../../DESIGN_PLAN.md) - System architecture
- [scripts/compare_tree.py](../../scripts/compare_tree.py) - Tree comparison tool

## License

[To be determined - should match repository license]
