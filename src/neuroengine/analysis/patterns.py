"""
Pattern detection utilities.

This module implements simple peak and threshold crossing detectors.  Such
functions are useful for identifying spikes or events in neural time
series.  For more sophisticated analyses consider using dedicated
libraries.
"""

from typing import Iterable, List

import numpy as np


def detect_peaks(signal: Iterable[float] | np.ndarray, threshold: float) -> List[int]:
    """Return indices of samples where the signal exceeds a threshold.

    Parameters
    ----------
    signal : iterable or ndarray
        Input 1D signal.
    threshold : float
        Amplitude above which a sample is considered a peak.

    Returns
    -------
    list of int
        Sorted list of indices where the signal crosses the threshold.
    """
    arr = np.asarray(signal, dtype=float)
    return [int(i) for i in np.where(arr > threshold)[0]]


def find_threshold_crossings(signal: Iterable[float] | np.ndarray, threshold: float) -> List[int]:
    """Detect points where the signal crosses a threshold from below.

    Parameters
    ----------
    signal : iterable or ndarray
        Input 1D signal.
    threshold : float
        Crossing threshold.

    Returns
    -------
    list of int
        Indices immediately after the threshold crossing.  For example,
        if `signal[i] <= threshold` and `signal[i+1] > threshold`, the
        returned list will include `i+1`.
    """
    arr = np.asarray(signal, dtype=float)
    crossings = []
    for i in range(len(arr) - 1):
        if arr[i] <= threshold < arr[i + 1]:
            crossings.append(i + 1)
    return crossings
