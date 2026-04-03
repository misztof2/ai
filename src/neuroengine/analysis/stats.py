"""
Statistical functions for neural signals.

This module provides lightweight wrappers around NumPy to compute basic
statistics.  These functions operate on 1D arrays by default but can
accept an axis argument where appropriate.
"""

from typing import Optional

import numpy as np


def mean(signal: np.ndarray, axis: Optional[int] = None) -> float | np.ndarray:
    """Compute the mean of a signal.

    Parameters
    ----------
    signal : ndarray
        Input array.
    axis : int, optional
        Axis along which to compute the mean.  If None, the mean of the
        flattened array is returned.

    Returns
    -------
    float or ndarray
        Mean value(s) along the specified axis.
    """
    return np.mean(signal, axis=axis)


def variance(signal: np.ndarray, axis: Optional[int] = None) -> float | np.ndarray:
    """Compute the variance of a signal.

    Parameters
    ----------
    signal : ndarray
        Input array.
    axis : int, optional
        Axis along which to compute the variance.

    Returns
    -------
    float or ndarray
        Variance value(s) along the specified axis.
    """
    return np.var(signal, axis=axis)


def autocorrelation(signal: np.ndarray, lag: int = 1) -> float:
    """Compute the autocorrelation of a 1D signal at a given lag.

    The autocorrelation is normalised by the variance such that
    autocorrelation at lag 0 is 1.

    Parameters
    ----------
    signal : ndarray
        1D input array.
    lag : int, optional
        Lag at which to compute the autocorrelation (default is 1).

    Returns
    -------
    float
        Autocorrelation coefficient at the specified lag.
    """
    if signal.ndim != 1:
        raise ValueError("autocorrelation expects a 1D signal")
    n = signal.size
    if lag < 0 or lag >= n:
        raise ValueError("lag must be non‑negative and less than the signal length")
    x = signal - np.mean(signal)
    denom = np.dot(x, x)
    if denom == 0:
        return 0.0
    return float(np.dot(x[:-lag], x[lag:]) / denom) if lag > 0 else 1.0
