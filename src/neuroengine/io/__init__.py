"""
I/O submodule for the Neuro Data Engine.

This package exposes functions to load data from common file formats
and to validate array shapes.  See `loaders.py` and `validation.py`
for implementation details.
"""

from .loaders import load_csv, load_numpy, load_yaml  # noqa: F401
from .validation import validate_array_shape  # noqa: F401

__all__ = ["load_csv", "load_numpy", "load_yaml", "validate_array_shape"]
