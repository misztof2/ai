"""
Plotting functions for neural data.

This module provides simple wrappers around matplotlib for common plot
types.  These wrappers ensure consistent labelling and styling across
different analyses.
"""

from typing import Iterable, Optional

import numpy as np
import matplotlib.pyplot as plt


def plot_trace(
    signal: Iterable[float] | np.ndarray,
    sampling_rate: Optional[float] = None,
    ax: Optional[plt.Axes] = None,
    **kwargs,
) -> plt.Axes:
    """Plot a 1D signal as a function of time.

    Parameters
    ----------
    signal : array-like
        The data to plot.
    sampling_rate : float, optional
        Sampling rate in Hertz.  If provided, the x‑axis will be scaled to
        seconds; otherwise sample index is used.
    ax : matplotlib.axes.Axes, optional
        Axes object to draw on.  If None, a new figure and axes will be
        created.
    kwargs : dict
        Additional keyword arguments passed to `ax.plot`.

    Returns
    -------
    matplotlib.axes.Axes
        The axes containing the plot.
    """
    arr = np.asarray(signal, dtype=float)
    if ax is None:
        fig, ax = plt.subplots()
    if sampling_rate is not None:
        x = np.arange(len(arr)) / float(sampling_rate)
        ax.set_xlabel("Time (s)")
    else:
        x = np.arange(len(arr))
        ax.set_xlabel("Sample index")
    ax.plot(x, arr, **kwargs)
    ax.set_ylabel("Amplitude")
    ax.set_title("Trace")
    return ax


def plot_histogram(
    data: Iterable[float] | np.ndarray,
    bins: int = 50,
    ax: Optional[plt.Axes] = None,
    **kwargs,
) -> plt.Axes:
    """Plot a histogram of the given data.

    Parameters
    ----------
    data : array-like
        Values to histogram.
    bins : int, optional
        Number of histogram bins (default is 50).
    ax : matplotlib.axes.Axes, optional
        Axes to draw on.  If None, a new figure and axes will be created.
    kwargs : dict
        Additional keyword arguments passed to `ax.hist`.

    Returns
    -------
    matplotlib.axes.Axes
        The axes containing the histogram.
    """
    arr = np.asarray(data, dtype=float)
    if ax is None:
        fig, ax = plt.subplots()
    ax.hist(arr, bins=bins, **kwargs)
    ax.set_xlabel("Value")
    ax.set_ylabel("Count")
    ax.set_title("Histogram")
    return ax
