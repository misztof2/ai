"""
Visualisation helpers for the Neuro Data Engine.

These functions wrap matplotlib to provide convenient plotting of traces
and distributions.  All plotting functions return matplotlib axes to
enable further customisation.
"""

from .plots import plot_trace, plot_histogram  # noqa: F401

__all__ = ["plot_trace", "plot_histogram"]
