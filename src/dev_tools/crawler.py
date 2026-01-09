"""
File Crawler Module

Traverses directory trees to collect file metadata and contents.
Supports filtering, ignoring patterns, and efficient tree navigation.
"""

import os
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Set, Callable
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class FileInfo:
    """Information about a file in the codebase"""
    path: str
    name: str
    size: int
    modified: float
    sha256: str
    extension: str
    lines: int
    is_binary: bool
    
    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return asdict(self)


class FileCrawler:
    """
    Crawls directory trees and collects file metadata.
    
    Features:
    - Recursive directory traversal
    - Configurable ignore patterns
    - SHA256 hash calculation for change detection
    - File metadata collection (size, lines, modified time)
    - Binary file detection
    """
    
    DEFAULT_IGNORE_PATTERNS = {
        '__pycache__', 'node_modules', 'venv', '.venv',
        'env', '.env', '.git', '.pytest_cache',
        'dist', 'build', '*.egg-info', '.DS_Store',
        '.idea', '.vscode', '*.pyc', '*.pyo', '*.pyd',
        '.coverage', 'htmlcov', '.tox', '.mypy_cache',
        '*.so', '*.dylib', '*.dll', '.eggs'
    }
    
    def __init__(
        self,
        root_path: str,
        ignore_patterns: Optional[Set[str]] = None,
        include_extensions: Optional[List[str]] = None,
        max_file_size: int = 10 * 1024 * 1024  # 10MB default
    ):
        """
        Initialize the file crawler.
        
        Args:
            root_path: Root directory to start crawling
            ignore_patterns: Set of patterns to ignore (adds to defaults)
            include_extensions: List of file extensions to include (None = all)
            max_file_size: Maximum file size to process (bytes)
        """
        self.root_path = Path(root_path).resolve()
        self.ignore_patterns = self.DEFAULT_IGNORE_PATTERNS.copy()
        if ignore_patterns:
            self.ignore_patterns.update(ignore_patterns)
        self.include_extensions = include_extensions
        self.max_file_size = max_file_size
        self._file_cache: Dict[str, FileInfo] = {}
        
    def crawl(self, update_callback: Optional[Callable[[str], None]] = None) -> Dict[str, FileInfo]:
        """
        Crawl the directory tree and collect file information.
        
        Args:
            update_callback: Optional callback function called for each file processed
            
        Returns:
            Dictionary mapping file paths to FileInfo objects
        """
        self._file_cache.clear()
        self._crawl_directory(self.root_path, update_callback)
        return self._file_cache
    
    def _crawl_directory(self, directory: Path, callback: Optional[Callable] = None):
        """Recursively crawl a directory"""
        try:
            for entry in sorted(directory.iterdir()):
                # Skip hidden files and ignore patterns
                if entry.name.startswith('.') or self._should_ignore(entry.name):
                    continue
                
                if entry.is_dir():
                    self._crawl_directory(entry, callback)
                elif entry.is_file():
                    # Check extension filter
                    if self.include_extensions and entry.suffix not in self.include_extensions:
                        continue
                    
                    # Check file size
                    try:
                        if entry.stat().st_size > self.max_file_size:
                            continue
                    except OSError:
                        continue
                    
                    # Process file
                    file_info = self._process_file(entry)
                    if file_info:
                        rel_path = str(entry.relative_to(self.root_path))
                        self._file_cache[rel_path] = file_info
                        
                        if callback:
                            callback(rel_path)
                            
        except PermissionError:
            # Skip directories we can't access
            pass
    
    def _should_ignore(self, name: str) -> bool:
        """Check if a file/directory should be ignored"""
        for pattern in self.ignore_patterns:
            if pattern.startswith('*'):
                # Wildcard pattern
                if name.endswith(pattern[1:]):
                    return True
            elif pattern.endswith('*'):
                # Wildcard pattern
                if name.startswith(pattern[:-1]):
                    return True
            else:
                # Exact match
                if name == pattern:
                    return True
        return False
    
    def _process_file(self, file_path: Path) -> Optional[FileInfo]:
        """Process a single file and extract metadata"""
        try:
            stat = file_path.stat()
            
            # Check if binary
            is_binary = self._is_binary_file(file_path)
            
            # Calculate SHA256
            sha256_hash = self._calculate_sha256(file_path)
            
            # Count lines for text files
            lines = 0
            if not is_binary:
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = sum(1 for _ in f)
                except:
                    pass
            
            return FileInfo(
                path=str(file_path),
                name=file_path.name,
                size=stat.st_size,
                modified=stat.st_mtime,
                sha256=sha256_hash,
                extension=file_path.suffix,
                lines=lines,
                is_binary=is_binary
            )
            
        except Exception as e:
            # Skip files we can't process
            return None
    
    def _is_binary_file(self, file_path: Path) -> bool:
        """Check if a file is binary"""
        # Common binary extensions
        binary_extensions = {
            '.pyc', '.pyo', '.so', '.dylib', '.dll',
            '.exe', '.bin', '.dat', '.db', '.sqlite',
            '.jpg', '.jpeg', '.png', '.gif', '.ico',
            '.pdf', '.zip', '.tar', '.gz', '.bz2',
            '.mp3', '.mp4', '.avi', '.mov'
        }
        
        if file_path.suffix.lower() in binary_extensions:
            return True
        
        # Check file content for binary data
        try:
            with open(file_path, 'rb') as f:
                chunk = f.read(1024)
                # Check for null bytes (common in binary files)
                return b'\x00' in chunk
        except:
            return True
    
    def _calculate_sha256(self, file_path: Path) -> str:
        """Calculate SHA256 hash of a file"""
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, 'rb') as f:
                # Read in chunks to handle large files
                for chunk in iter(lambda: f.read(4096), b''):
                    sha256_hash.update(chunk)
            return sha256_hash.hexdigest()
        except:
            return ""
    
    def get_tree_structure(self) -> Dict:
        """
        Get a hierarchical tree structure of the crawled files.
        
        Returns:
            Dictionary representing the directory tree
        """
        tree = {}
        
        for rel_path, file_info in self._file_cache.items():
            parts = Path(rel_path).parts
            current = tree
            
            # Build nested structure
            for i, part in enumerate(parts):
                if i == len(parts) - 1:
                    # This is a file
                    current[part] = {
                        'type': 'file',
                        'info': file_info.to_dict()
                    }
                else:
                    # This is a directory
                    if part not in current:
                        current[part] = {'type': 'directory', 'children': {}}
                    current = current[part]['children']
        
        return tree
    
    def get_statistics(self) -> Dict:
        """
        Get statistics about the crawled files.
        
        Returns:
            Dictionary with statistics
        """
        total_files = len(self._file_cache)
        total_size = sum(f.size for f in self._file_cache.values())
        total_lines = sum(f.lines for f in self._file_cache.values() if not f.is_binary)
        
        extensions = {}
        for file_info in self._file_cache.values():
            ext = file_info.extension or 'no_extension'
            extensions[ext] = extensions.get(ext, 0) + 1
        
        return {
            'total_files': total_files,
            'total_size': total_size,
            'total_lines': total_lines,
            'binary_files': sum(1 for f in self._file_cache.values() if f.is_binary),
            'text_files': sum(1 for f in self._file_cache.values() if not f.is_binary),
            'extensions': extensions,
            'crawl_time': datetime.now().isoformat()
        }
