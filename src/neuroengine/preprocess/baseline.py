"""
Baseline correction utilities.

Baseline drifts in neural signals (e.g. due to motion artefacts or slow
physiological changes) can obscure relevant events.  The functions here
apply a moving average or median filter to estimate the baseline and
subtract it from the original signal.
"""

from typing import Union

import numpy as np


def baseline_correction(signal: Union[np.ndarray, list], window: int = 100) -> np.ndarray:
    """Subtract a moving average baseline from a signal.

    This function computes a simple moving average over a specified window
    (in samples) and subtracts it from the input signal to remove slow
    drifts.  For multichannel data (2D array), the baseline is computed
    independently for each channel.

    Parameters
    ----------
    signal : array-like
        Input signal as a 1D or 2D array.  If 2D, rows are interpreted as
        channels and columns as time points (or vice versa).
    window : int, optional
        Length of the moving average window in samples.  Larger values
        produce smoother baselines.  Default is 100.

    Returns
    -------
    ndarray
        Baseline-corrected signal of the same shape as the input.

    Raises
    ------
    ValueError
        If `window` is not a positive integer or larger than the signal length.
    """
    arr = np.asarray(signal, dtype=float)
    if window <= 0:
        raise ValueError("window must be a positive integer")
    if arr.ndim == 1:
        if window > arr.size:
            raise ValueError("window length cannot exceed signal length")
        # Compute moving average using convolution
        kernel = np.ones(window) / window
        baseline = np.convolve(arr, kernel, mode="same")
        return arr - baseline
    elif arr.ndim == 2:
        corrected = np.empty_like(arr)
        for i in range(arr.shape[0]):
            if window > arr.shape[1]:
                raise ValueError("window length cannot exceed signal length")
            kernel = np.ones(window) / window
            baseline = np.convolve(arr[i], kernel, mode="same")
            corrected[i] = arr[i] - baseline
        return corrected
    else:
        raise ValueError("signal must be 1D or 2D array-like")
