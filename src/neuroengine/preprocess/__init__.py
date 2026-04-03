"""
Preprocessing routines for the Neuro Data Engine.

This package includes functions for baseline correction, normalisation and
digital filtering.  Use these utilities to clean your raw signals before
statistical analysis.
"""

from .baseline import baseline_correction  # noqa: F401
from .normalization import zscore_normalization, minmax_normalization  # noqa: F401
from .filters import lowpass_filter, highpass_filter  # noqa: F401

__all__ = [
    "baseline_correction",
    "zscore_normalization",
    "minmax_normalization",
    "lowpass_filter",
    "highpass_filter",
]
