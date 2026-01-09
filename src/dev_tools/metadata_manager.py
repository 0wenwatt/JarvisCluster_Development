"""
Metadata Manager Module

Manages file metadata with SHA256 hashing for change detection.
Tracks dependencies and provides up-to-date status checking.
"""

import json
import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Set
from datetime import datetime
from dataclasses import dataclass, asdict


@dataclass
class DependencyInfo:
    """Information about a dependency"""
    name: str
    path: str
    sha256: str
    last_modified: float
    
    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class NodeMetadata:
    """Metadata for a node (file or directory)"""
    path: str
    name: str
    sha256: str
    last_modified: float
    last_checked: float
    dependencies: List[str]  # List of dependency paths
    up_to_date: bool
    
    def to_dict(self) -> dict:
        return asdict(self)


class MetadataManager:
    """
    Manages metadata for files and their dependencies.
    
    Features:
    - SHA256-based change detection
    - Dependency tracking
    - Up-to-date status checking
    - Persistent metadata storage
    - Efficient change detection
    """
    
    def __init__(self, metadata_file: str = ".jarvis_metadata.json"):
        """
        Initialize the metadata manager.
        
        Args:
            metadata_file: Path to the metadata storage file
        """
        self.metadata_file = Path(metadata_file)
        self.metadata: Dict[str, NodeMetadata] = {}
        self.dependencies: Dict[str, List[DependencyInfo]] = {}
        self._load_metadata()
    
    def _load_metadata(self):
        """Load metadata from file"""
        if self.metadata_file.exists():
            try:
                with open(self.metadata_file, 'r') as f:
                    data = json.load(f)
                    
                # Load node metadata
                for path, node_data in data.get('nodes', {}).items():
                    self.metadata[path] = NodeMetadata(**node_data)
                
                # Load dependencies
                for path, deps_data in data.get('dependencies', {}).items():
                    self.dependencies[path] = [
                        DependencyInfo(**dep) for dep in deps_data
                    ]
            except (json.JSONDecodeError, TypeError) as e:
                # If metadata is corrupted, start fresh
                self.metadata = {}
                self.dependencies = {}
    
    def save_metadata(self):
        """Save metadata to file"""
        data = {
            'version': '1.0',
            'last_updated': datetime.now().isoformat(),
            'nodes': {
                path: node.to_dict() 
                for path, node in self.metadata.items()
            },
            'dependencies': {
                path: [dep.to_dict() for dep in deps]
                for path, deps in self.dependencies.items()
            }
        }
        
        # Ensure parent directory exists
        self.metadata_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.metadata_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def update_node(
        self,
        path: str,
        sha256: str,
        last_modified: float,
        dependencies: Optional[List[str]] = None
    ):
        """
        Update metadata for a node.
        
        Args:
            path: Path to the file/directory
            sha256: SHA256 hash of the content
            last_modified: Last modification timestamp
            dependencies: List of dependency paths
        """
        current_time = datetime.now().timestamp()
        
        # Check if node is up to date
        up_to_date = True
        if path in self.metadata:
            old_node = self.metadata[path]
            up_to_date = (
                old_node.sha256 == sha256 and
                old_node.last_modified == last_modified
            )
        
        self.metadata[path] = NodeMetadata(
            path=path,
            name=Path(path).name,
            sha256=sha256,
            last_modified=last_modified,
            last_checked=current_time,
            dependencies=dependencies or [],
            up_to_date=up_to_date
        )
    
    def add_dependency(
        self,
        node_path: str,
        dependency_path: str,
        dependency_sha256: str,
        dependency_modified: float
    ):
        """
        Add a dependency for a node.
        
        Args:
            node_path: Path to the node
            dependency_path: Path to the dependency
            dependency_sha256: SHA256 hash of the dependency
            dependency_modified: Last modification time of dependency
        """
        if node_path not in self.dependencies:
            self.dependencies[node_path] = []
        
        # Check if dependency already exists
        for dep in self.dependencies[node_path]:
            if dep.path == dependency_path:
                # Update existing dependency
                dep.sha256 = dependency_sha256
                dep.last_modified = dependency_modified
                return
        
        # Add new dependency
        self.dependencies[node_path].append(DependencyInfo(
            name=Path(dependency_path).name,
            path=dependency_path,
            sha256=dependency_sha256,
            last_modified=dependency_modified
        ))
    
    def is_up_to_date(self, path: str) -> bool:
        """
        Check if a node is up to date.
        
        Args:
            path: Path to check
            
        Returns:
            True if up to date, False otherwise
        """
        if path not in self.metadata:
            return False
        
        node = self.metadata[path]
        
        # Check if file still exists and hasn't changed
        file_path = Path(path)
        if not file_path.exists():
            return False
        
        # Check file modification time
        try:
            stat = file_path.stat()
            if stat.st_mtime != node.last_modified:
                return False
        except OSError:
            return False
        
        # Check dependencies
        if path in self.dependencies:
            for dep in self.dependencies[path]:
                if not self._is_dependency_up_to_date(dep):
                    return False
        
        return True
    
    def _is_dependency_up_to_date(self, dependency: DependencyInfo) -> bool:
        """Check if a dependency is up to date"""
        dep_path = Path(dependency.path)
        if not dep_path.exists():
            return False
        
        try:
            stat = dep_path.stat()
            if stat.st_mtime != dependency.last_modified:
                return False
            
            # Calculate current hash
            current_hash = self._calculate_file_hash(dep_path)
            if current_hash != dependency.sha256:
                return False
        except OSError:
            return False
        
        return True
    
    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA256 hash of a file"""
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    sha256_hash.update(chunk)
            return sha256_hash.hexdigest()
        except:
            return ""
    
    def get_outdated_nodes(self) -> List[str]:
        """
        Get list of outdated nodes.
        
        Returns:
            List of paths to outdated nodes
        """
        outdated = []
        for path in self.metadata.keys():
            if not self.is_up_to_date(path):
                outdated.append(path)
        return outdated
    
    def get_changed_files(self, base_path: str = ".") -> Dict[str, str]:
        """
        Get files that have changed since last check.
        
        Args:
            base_path: Base directory to check
            
        Returns:
            Dictionary mapping file paths to change status
        """
        changed = {}
        base = Path(base_path)
        
        for path, node in self.metadata.items():
            full_path = base / path
            if not full_path.exists():
                changed[path] = 'deleted'
                continue
            
            try:
                current_hash = self._calculate_file_hash(full_path)
                if current_hash != node.sha256:
                    changed[path] = 'modified'
            except:
                changed[path] = 'error'
        
        return changed
    
    def get_dependency_chain(self, path: str) -> Set[str]:
        """
        Get the full dependency chain for a node.
        
        Args:
            path: Path to the node
            
        Returns:
            Set of all dependency paths (recursive)
        """
        chain = set()
        self._build_dependency_chain(path, chain)
        return chain
    
    def _build_dependency_chain(self, path: str, chain: Set[str]):
        """Recursively build dependency chain"""
        if path in self.dependencies:
            for dep in self.dependencies[path]:
                if dep.path not in chain:
                    chain.add(dep.path)
                    self._build_dependency_chain(dep.path, chain)
    
    def get_statistics(self) -> Dict:
        """
        Get statistics about the metadata.
        
        Returns:
            Dictionary with statistics
        """
        total_nodes = len(self.metadata)
        up_to_date_nodes = sum(1 for path in self.metadata if self.is_up_to_date(path))
        total_dependencies = sum(len(deps) for deps in self.dependencies.values())
        
        return {
            'total_nodes': total_nodes,
            'up_to_date_nodes': up_to_date_nodes,
            'outdated_nodes': total_nodes - up_to_date_nodes,
            'total_dependencies': total_dependencies,
            'last_updated': datetime.now().isoformat()
        }
    
    def clear(self):
        """Clear all metadata"""
        self.metadata.clear()
        self.dependencies.clear()
    
    def remove_node(self, path: str):
        """Remove a node from metadata"""
        if path in self.metadata:
            del self.metadata[path]
        if path in self.dependencies:
            del self.dependencies[path]
