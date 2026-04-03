"""
Signal abstractions for neural data.

This package defines a simple `Trace` class representing a single
continuous recording as well as any helper functions for manipulating
collections of traces.
"""

from .traces import Trace  # noqa: F401

__all__ = ["Trace"]
