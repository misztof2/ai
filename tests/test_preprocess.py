"""
Tests for preprocessing functions.
"""

import numpy as np
import pytest

from neuroengine.preprocess import baseline_correction, zscore_normalization, minmax_normalization


def test_baseline_correction_constant_signal():
    # A constant signal should become zero after baseline correction
    signal = np.ones(100)
    corrected = baseline_correction(signal, window=10)
    # Because of edge effects, small numerical errors may appear; use tolerance
    assert np.allclose(corrected, 0.0, atol=1e-3)


def test_zscore_normalization():
    signal = np.array([1.0, 2.0, 3.0])
    normalized = zscore_normalization(signal)
    # Check mean ~ 0 and std ~ 1
    assert abs(np.mean(normalized)) < 1e-7
    assert abs(np.std(normalized) - 1.0) < 1e-7


def test_minmax_normalization():
    signal = np.array([1.0, 2.0, 3.0])
    scaled = minmax_normalization(signal)
    assert np.allclose(scaled, [0.0, 0.5, 1.0])
