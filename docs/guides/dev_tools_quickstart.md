# Development Tools Quick Start Guide

This guide shows you how to quickly get started with the Jarvis development tools.

## What Are These Tools?

The `src/dev_tools/` package provides utilities for:

- **Crawling** codebases to collect file metadata and statistics
- **Tracking** changes using SHA256 hashing
- **Querying** code to extract functions, classes, and snippets
- **Formatting** code for LLM (AI assistant) consumption
- **Managing** dependencies between files

## Quick Start (3 minutes)

### 1. Crawl a Directory

Collect information about all files in a directory:

```bash
cd src/dev_tools
python3 cli.py crawl ../../scripts -o /tmp/crawl_output.json
```

This will show you:
- Total files and size
- Lines of code
- File type breakdown
- Binary vs text files

### 2. Track Changes

Create a metadata baseline to track changes:

```bash
# First, create the baseline
python3 cli.py metadata update -p ../../scripts

# Later, check what's changed
python3 cli.py metadata check -p ../../scripts
```

This helps you:
- Detect modified files
- Track dependencies
- Know when to rebuild/retest

### 3. Query Code

Extract information from your code:

```bash
# Get a file summary
python3 cli.py query summary -p ../.. -f scripts/compare_tree.py

# Extract all functions
python3 cli.py query functions -p ../.. -f scripts/compare_tree.py

# Search for patterns
python3 cli.py query search --pattern "class.*Crawler" --file-pattern "**/*.py"
```

### 4. Format for AI

Get LLM-friendly output for AI coding assistants:

```bash
# Format a file for LLM consumption
python3 cli.py query llm -p ../.. -f scripts/compare_tree.py -o /tmp/context.txt

# Then paste context.txt into your AI assistant
```

## Use Cases

### For Development

**Track which files changed during development:**
```bash
# Before starting work
python3 cli.py metadata update

# After making changes
python3 cli.py metadata check
# Shows exactly what you modified
```

**Find similar code patterns:**
```bash
python3 cli.py query search --pattern "def.*schedule" --context 5
# Finds all functions with "schedule" in their name
```

### For LLM/AI Assistance

**Provide context to AI assistant:**
```bash
# Extract relevant files with full context
python3 cli.py query llm -f src/scheduler.py -o scheduler_context.txt

# Copy scheduler_context.txt and paste into ChatGPT/Claude/etc
# Now the AI understands your codebase!
```

**Find examples to show AI:**
```bash
# Find all error handling patterns
python3 cli.py query search --pattern "except.*Error" --context 3
```

### For Code Review

**Get overview before reviewing:**
```bash
# Quick summary
python3 cli.py query summary -f path/to/file.py

# See all functions
python3 cli.py query functions -f path/to/file.py
```

**Check dependencies:**
```bash
python3 cli.py metadata update
# Now you can see what each file depends on
```

## Interactive Examples

Run the interactive example script:

```bash
cd src/dev_tools
python3 example_usage.py
```

This walks you through:
1. Crawling a codebase
2. Tracking metadata
3. Querying files
4. LLM formatting
5. Pattern searching
6. Dependency tracking

## Python API

Use the tools in your own scripts:

```python
from dev_tools import FileCrawler, MetadataManager, CodebaseQueryInterface

# Crawl
crawler = FileCrawler(root_path="/path/to/code")
files = crawler.crawl()
stats = crawler.get_statistics()

# Track changes
metadata = MetadataManager()
metadata.update_node(path="file.py", sha256="...", last_modified=123456)
is_current = metadata.is_up_to_date("file.py")

# Query
query = CodebaseQueryInterface(root_path="/path/to/code")
functions = query.extract_functions("file.py")
summary = query.get_file_summary("file.py")
```

## Common Commands Reference

```bash
# Crawl commands
python3 cli.py crawl <directory>                    # Basic crawl
python3 cli.py crawl <directory> -v                 # Verbose
python3 cli.py crawl <directory> -o output.json     # Save to JSON

# Metadata commands
python3 cli.py metadata update                      # Update baseline
python3 cli.py metadata check                       # Check changes
python3 cli.py metadata stats                       # Show statistics

# Query commands
python3 cli.py query file -f <file>                 # View file
python3 cli.py query functions -f <file>            # Extract functions
python3 cli.py query classes -f <file>              # Extract classes
python3 cli.py query summary -f <file>              # File summary
python3 cli.py query search --pattern <regex>       # Search
python3 cli.py query llm -f <file> -o output.txt    # LLM format
```

## Next Steps

1. **Read the full documentation**: [src/dev_tools/README.md](src/dev_tools/README.md)
2. **Try the examples**: `python3 example_usage.py`
3. **Use in your workflow**: Integrate into your daily development
4. **Customize**: Modify for your specific needs

## Tips

- Use `-v` for verbose output to see what's happening
- Use `-o` to save results to files for later analysis
- Combine with `git diff` to understand your changes
- Use metadata tracking before and after major refactoring
- Format code for LLM when you need AI assistance with complex files

## Need Help?

- Check `python3 cli.py --help` for all commands
- See `python3 cli.py <command> --help` for command-specific help
- Read [src/dev_tools/README.md](src/dev_tools/README.md) for detailed documentation
- Look at [example_usage.py](src/dev_tools/example_usage.py) for code examples
