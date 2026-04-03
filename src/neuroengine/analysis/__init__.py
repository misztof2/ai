"""
Analysis routines for the Neuro Data Engine.

This package exposes simple statistical functions and pattern detection
utilities.  You can extend these modules with your own algorithms as
needed.
"""

from .stats import mean, variance, autocorrelation  # noqa: F401
from .patterns import detect_peaks, find_threshold_crossings  # noqa: F401

__all__ = [
    "mean",
    "variance",
    "autocorrelation",
    "detect_peaks",
    "find_threshold_crossings",
]
