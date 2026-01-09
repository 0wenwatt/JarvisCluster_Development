"""
Codebase Query Interface Module

Provides an LLM-friendly interface for querying the codebase.
Extracts code snippets, presents file contents, and helps navigate the codebase.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict


@dataclass
class CodeSnippet:
    """A code snippet from the codebase"""
    file_path: str
    start_line: int
    end_line: int
    content: str
    context: str  # function/class name, or other context
    snippet_type: str  # 'function', 'class', 'import', 'comment', 'block'
    
    def to_dict(self) -> dict:
        return asdict(self)


class CodebaseQueryInterface:
    """
    Interface for querying and presenting codebase information.
    
    Features:
    - File content retrieval
    - Code snippet extraction (functions, classes, etc.)
    - Context-aware code presentation
    - Search by pattern
    - LLM-optimized output formatting
    """
    
    def __init__(self, root_path: str):
        """
        Initialize the query interface.
        
        Args:
            root_path: Root directory of the codebase
        """
        self.root_path = Path(root_path).resolve()
    
    def get_file_content(
        self,
        file_path: str,
        start_line: Optional[int] = None,
        end_line: Optional[int] = None,
        max_lines: int = 1000
    ) -> Optional[str]:
        """
        Get content of a file or a portion of it.
        
        Args:
            file_path: Path to the file (relative to root)
            start_line: Starting line number (1-indexed)
            end_line: Ending line number (1-indexed)
            max_lines: Maximum lines to return
            
        Returns:
            File content or None if file not found
        """
        full_path = self.root_path / file_path
        if not full_path.exists() or not full_path.is_file():
            return None
        
        try:
            with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            
            # Apply line range
            if start_line is not None:
                start_idx = max(0, start_line - 1)
            else:
                start_idx = 0
            
            if end_line is not None:
                end_idx = min(len(lines), end_line)
            else:
                end_idx = len(lines)
            
            # Apply max_lines limit
            if end_idx - start_idx > max_lines:
                end_idx = start_idx + max_lines
            
            selected_lines = lines[start_idx:end_idx]
            
            # Add line numbers
            numbered_lines = []
            for i, line in enumerate(selected_lines, start=start_idx + 1):
                numbered_lines.append(f"{i:4d} | {line.rstrip()}")
            
            return '\n'.join(numbered_lines)
            
        except Exception as e:
            return None
    
    def extract_functions(self, file_path: str) -> List[CodeSnippet]:
        """
        Extract all functions from a Python file.
        
        Args:
            file_path: Path to the Python file
            
        Returns:
            List of CodeSnippet objects for each function
        """
        full_path = self.root_path / file_path
        if not full_path.exists():
            return []
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except:
            return []
        
        snippets = []
        in_function = False
        func_start = 0
        func_name = ""
        func_indent = 0
        
        for i, line in enumerate(lines, start=1):
            # Detect function definition
            func_match = re.match(r'^(\s*)def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', line)
            if func_match:
                # Save previous function if any
                if in_function:
                    content = ''.join(lines[func_start-1:i-1])
                    snippets.append(CodeSnippet(
                        file_path=file_path,
                        start_line=func_start,
                        end_line=i-1,
                        content=content.rstrip(),
                        context=func_name,
                        snippet_type='function'
                    ))
                
                # Start new function
                in_function = True
                func_start = i
                func_name = func_match.group(2)
                func_indent = len(func_match.group(1))
            
            elif in_function and line.strip():
                # Calculate current line's indent
                current_indent = len(line) - len(line.lstrip())
                
                # Function ends when we see a line at the same or lower indent level
                # (but not inside the function body)
                if current_indent <= func_indent:
                    # Function ended
                    content = ''.join(lines[func_start-1:i-1])
                    snippets.append(CodeSnippet(
                        file_path=file_path,
                        start_line=func_start,
                        end_line=i-1,
                        content=content.rstrip(),
                        context=func_name,
                        snippet_type='function'
                    ))
                    in_function = False
        
        # Save last function if file ended during function
        if in_function:
            content = ''.join(lines[func_start-1:])
            snippets.append(CodeSnippet(
                file_path=file_path,
                start_line=func_start,
                end_line=len(lines),
                content=content.rstrip(),
                context=func_name,
                snippet_type='function'
            ))
        
        return snippets
    
    def extract_classes(self, file_path: str) -> List[CodeSnippet]:
        """
        Extract all classes from a Python file.
        
        Args:
            file_path: Path to the Python file
            
        Returns:
            List of CodeSnippet objects for each class
        """
        full_path = self.root_path / file_path
        if not full_path.exists():
            return []
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except:
            return []
        
        snippets = []
        in_class = False
        class_start = 0
        class_name = ""
        class_indent = 0
        
        for i, line in enumerate(lines, start=1):
            # Detect class definition
            class_match = re.match(r'^(\s*)class\s+([a-zA-Z_][a-zA-Z0-9_]*)', line)
            if class_match:
                # Save previous class if any
                if in_class:
                    content = ''.join(lines[class_start-1:i-1])
                    snippets.append(CodeSnippet(
                        file_path=file_path,
                        start_line=class_start,
                        end_line=i-1,
                        content=content.rstrip(),
                        context=class_name,
                        snippet_type='class'
                    ))
                
                # Start new class
                in_class = True
                class_start = i
                class_name = class_match.group(2)
                class_indent = len(class_match.group(1))
            
            elif in_class and line.strip():
                # Calculate current line's indent
                current_indent = len(line) - len(line.lstrip())
                
                # Class ends when we see a line at the same or lower indent level
                # (but not inside the class body)
                if current_indent <= class_indent:
                    # Class ended
                    content = ''.join(lines[class_start-1:i-1])
                    snippets.append(CodeSnippet(
                        file_path=file_path,
                        start_line=class_start,
                        end_line=i-1,
                        content=content.rstrip(),
                        context=class_name,
                        snippet_type='class'
                    ))
                    in_class = False
        
        # Save last class if file ended during class
        if in_class:
            content = ''.join(lines[class_start-1:])
            snippets.append(CodeSnippet(
                file_path=file_path,
                start_line=class_start,
                end_line=len(lines),
                content=content.rstrip(),
                context=class_name,
                snippet_type='class'
            ))
        
        return snippets
    
    def search_pattern(
        self,
        pattern: str,
        file_pattern: str = "*.py",
        context_lines: int = 3
    ) -> List[CodeSnippet]:
        """
        Search for a pattern in the codebase.
        
        Args:
            pattern: Regular expression pattern to search
            file_pattern: Glob pattern for files to search
            context_lines: Number of context lines to include
            
        Returns:
            List of CodeSnippet objects with matches
        """
        snippets = []
        compiled_pattern = re.compile(pattern)
        
        for file_path in self.root_path.rglob(file_pattern):
            if not file_path.is_file():
                continue
            
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
            except:
                continue
            
            for i, line in enumerate(lines, start=1):
                if compiled_pattern.search(line):
                    # Extract context
                    start = max(0, i - context_lines - 1)
                    end = min(len(lines), i + context_lines)
                    content = ''.join(lines[start:end])
                    
                    rel_path = str(file_path.relative_to(self.root_path))
                    snippets.append(CodeSnippet(
                        file_path=rel_path,
                        start_line=start + 1,
                        end_line=end,
                        content=content.rstrip(),
                        context=f"Match at line {i}",
                        snippet_type='block'
                    ))
        
        return snippets
    
    def get_imports(self, file_path: str) -> List[str]:
        """
        Extract all import statements from a Python file.
        
        Args:
            file_path: Path to the Python file
            
        Returns:
            List of import statements
        """
        full_path = self.root_path / file_path
        if not full_path.exists():
            return []
        
        imports = []
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('import ') or line.startswith('from '):
                        imports.append(line)
        except:
            pass
        
        return imports
    
    def format_for_llm(
        self,
        file_path: str,
        include_functions: bool = True,
        include_classes: bool = True,
        max_content_length: int = 5000
    ) -> str:
        """
        Format file information for LLM consumption.
        
        Args:
            file_path: Path to the file
            include_functions: Include function extraction
            include_classes: Include class extraction
            max_content_length: Maximum content length
            
        Returns:
            Formatted string for LLM
        """
        output = []
        output.append(f"# File: {file_path}")
        output.append("")
        
        # Get file content
        content = self.get_file_content(file_path)
        if not content:
            output.append("*File not found or cannot be read*")
            return '\n'.join(output)
        
        # Truncate if too long
        if len(content) > max_content_length:
            content = content[:max_content_length] + "\n... (truncated)"
        
        output.append("## Full Content")
        output.append("```")
        output.append(content)
        output.append("```")
        output.append("")
        
        # Extract imports
        imports = self.get_imports(file_path)
        if imports:
            output.append("## Imports")
            for imp in imports:
                output.append(f"- {imp}")
            output.append("")
        
        # Extract functions
        if include_functions:
            functions = self.extract_functions(file_path)
            if functions:
                output.append("## Functions")
                for func in functions:
                    output.append(f"- `{func.context}()` (lines {func.start_line}-{func.end_line})")
                output.append("")
        
        # Extract classes
        if include_classes:
            classes = self.extract_classes(file_path)
            if classes:
                output.append("## Classes")
                for cls in classes:
                    output.append(f"- `{cls.context}` (lines {cls.start_line}-{cls.end_line})")
                output.append("")
        
        return '\n'.join(output)
    
    def get_file_summary(self, file_path: str) -> Dict:
        """
        Get a summary of a file's contents.
        
        Args:
            file_path: Path to the file
            
        Returns:
            Dictionary with file summary
        """
        full_path = self.root_path / file_path
        if not full_path.exists():
            return {'error': 'File not found'}
        
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except:
            return {'error': 'Cannot read file'}
        
        functions = self.extract_functions(file_path)
        classes = self.extract_classes(file_path)
        imports = self.get_imports(file_path)
        
        return {
            'path': file_path,
            'lines': len(lines),
            'functions': [f.context for f in functions],
            'classes': [c.context for c in classes],
            'imports': imports,
            'size': full_path.stat().st_size
        }
