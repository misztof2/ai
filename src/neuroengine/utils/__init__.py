"""
Utility functions for the Neuro Data Engine.

This package contains small helpers that do not fit into other modules
but are widely used across the project.
"""

from .paths import get_data_path, get_results_path  # noqa: F401

__all__ = ["get_data_path", "get_results_path"]
