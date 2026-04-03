"""
Neuro Data Engine core package.

This package provides a modular pipeline for loading, preprocessing, analysing
and visualising neural recording data.  Subpackages implement distinct
functional layers and are imported below for convenience.
"""

from . import io, preprocess, signals, analysis, visualization, export, utils  # noqa: F401

__all__ = [
    "io",
    "preprocess",
    "signals",
    "analysis",
    "visualization",
    "export",
    "utils",
]
