"""
Normalisation utilities for neural signals.

Two common normalisation strategies are provided: z-score normalisation,
which rescales data to zero mean and unit variance, and min–max
normalisation, which rescales values to the range [0, 1].
"""

from typing import Union

import numpy as np


def zscore_normalization(signal: Union[np.ndarray, list], axis: int = -1) -> np.ndarray:
    """Perform z-score normalisation on a signal.

    For each sample (along the specified axis) the mean is subtracted and
    the result is divided by the standard deviation.  If the standard
    deviation is zero (constant signal) the function returns zeros.

    Parameters
    ----------
    signal : array-like
        Input data to normalise.
    axis : int, optional
        Axis along which to compute statistics (default is last axis).

    Returns
    -------
    ndarray
        Normalised data with zero mean and unit variance along the
        specified axis.
    """
    arr = np.asarray(signal, dtype=float)
    mean = np.mean(arr, axis=axis, keepdims=True)
    std = np.std(arr, axis=axis, keepdims=True)
    std_safe = np.where(std == 0, 1.0, std)
    return (arr - mean) / std_safe


def minmax_normalization(signal: Union[np.ndarray, list], axis: int = -1) -> np.ndarray:
    """Rescale data to the range [0, 1].

    Parameters
    ----------
    signal : array-like
        Input data to rescale.
    axis : int, optional
        Axis along which to compute minima and maxima.

    Returns
    -------
    ndarray
        Rescaled data.
    """
    arr = np.asarray(signal, dtype=float)
    min_val = np.min(arr, axis=axis, keepdims=True)
    max_val = np.max(arr, axis=axis, keepdims=True)
    range_val = max_val - min_val
    range_safe = np.where(range_val == 0, 1.0, range_val)
    return (arr - min_val) / range_safe
