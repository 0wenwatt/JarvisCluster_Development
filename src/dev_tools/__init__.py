"""
Development Tools for JarvisCluster

This package provides tools for development, including:
- File crawling and metadata collection
- SHA256-based change detection
- Code snippet extraction
- LLM-friendly codebase querying
"""

__version__ = "0.1.0"

from .crawler import FileCrawler
from .metadata_manager import MetadataManager
from .query_interface import CodebaseQueryInterface

__all__ = [
    'FileCrawler',
    'MetadataManager', 
    'CodebaseQueryInterface',
]
