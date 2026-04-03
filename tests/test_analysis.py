"""
Tests for analysis functions.
"""

import numpy as np

from neuroengine.analysis import mean, variance, autocorrelation, detect_peaks, find_threshold_crossings


def test_mean_and_variance():
    data = np.array([1.0, 2.0, 3.0, 4.0])
    assert mean(data) == 2.5
    assert variance(data) == np.var(data)


def test_autocorrelation():
    # Simple signal where autocorrelation at lag 1 is known
    data = np.array([1.0, -1.0, 1.0, -1.0])
    # For this alternating pattern, mean=0 and autocorrelation at lag 1 = -1
    assert abs(autocorrelation(data, lag=1) + 1.0) < 1e-7
    assert autocorrelation(data, lag=0) == 1.0


def test_detect_peaks_and_crossings():
    signal = np.array([0.0, 1.0, 3.0, 2.0, 0.5, 2.5, 0.0])
    peaks = detect_peaks(signal, threshold=2.0)
    # Peaks above 2.0 occur at indices 2 and 5
    assert peaks == [2, 5]
    crossings = find_threshold_crossings(signal, threshold=1.0)
    # Threshold crossing from below occurs at 1->2 and 4->5
    assert crossings == [2, 5]
