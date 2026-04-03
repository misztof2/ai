"""
Digital filters for neural signals.

This module wraps SciPy's Butterworth filters to implement basic low‑pass
and high‑pass filtering.  If SciPy is unavailable, the functions will
raise an ImportError.  Filtering is performed forward and backward
(`filtfilt`) to avoid phase distortions.
"""

from typing import Sequence, Union

import numpy as np

try:
    from scipy.signal import butter, filtfilt  # type: ignore
except ImportError as exc:
    raise ImportError(
        "SciPy is required for filtering functions; please install scipy"
    ) from exc


def _butter_filter(
    signal: Union[np.ndarray, Sequence[float]],
    cutoff: float,
    fs: float,
    order: int,
    btype: str,
) -> np.ndarray:
    """Internal helper to apply a Butterworth filter."""
    arr = np.asarray(signal, dtype=float)
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(N=order, Wn=normal_cutoff, btype=btype, analog=False)
    return filtfilt(b, a, arr)


def lowpass_filter(
    signal: Union[np.ndarray, Sequence[float]],
    cutoff: float,
    fs: float,
    order: int = 2,
) -> np.ndarray:
    """Apply a low‑pass Butterworth filter to a signal.

    Parameters
    ----------
    signal : array-like
        Input signal to filter.
    cutoff : float
        Cutoff frequency in Hertz.
    fs : float
        Sampling rate of the signal in Hertz.
    order : int, optional
        Order of the Butterworth filter (default is 2).

    Returns
    -------
    ndarray
        Filtered signal of the same shape as the input.
    """
    return _butter_filter(signal, cutoff, fs, order, btype="low")


def highpass_filter(
    signal: Union[np.ndarray, Sequence[float]],
    cutoff: float,
    fs: float,
    order: int = 2,
) -> np.ndarray:
    """Apply a high‑pass Butterworth filter to a signal.

    See `lowpass_filter` for parameter descriptions.
    """
    return _butter_filter(signal, cutoff, fs, order, btype="high")
