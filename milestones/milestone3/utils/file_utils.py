"""Utility functions for file and path operations."""

import os

def resolve_path(path: str) -> str:
    """
    Resolve relative path to absolute path relative to the project root (milestone3).
    
    Args:
        path: Input path (relative or absolute)
        
    Returns:
        Absolute path
    """
    if os.path.isabs(path):
        return path
    
    # Get the directory where this file is located (milestones/milestone3/utils/)
    # Go up two levels to get to milestones/milestone3/
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, path)
