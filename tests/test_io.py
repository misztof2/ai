"""
Tests for I/O utilities.
"""

import os
import tempfile

import numpy as np
import pytest

from neuroengine.io import load_csv, load_numpy, load_yaml, validate_array_shape


def test_load_csv_and_numpy(tmp_path):
    # Create a temporary CSV file
    csv_path = tmp_path / "test.csv"
    arr = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    np.savetxt(csv_path, arr, delimiter=",")
    loaded = load_csv(csv_path)
    assert np.allclose(loaded, arr)

    # Save and load numpy file
    npy_path = tmp_path / "test.npy"
    np.save(npy_path, arr)
    loaded_npy = load_numpy(npy_path)
    assert np.allclose(loaded_npy, arr)


def test_load_yaml(tmp_path):
    yaml_path = tmp_path / "config.yaml"
    content = """
    foo: 1
    bar:
      baz: true
    """
    yaml_path.write_text(content)
    cfg = load_yaml(yaml_path)
    assert cfg["foo"] == 1
    assert cfg["bar"]["baz"] is True


def test_validate_array_shape():
    arr1 = np.zeros(10)
    arr2 = np.zeros((2, 3))
    # Correct dimensions should not raise
    validate_array_shape(arr1, 1)
    validate_array_shape(arr2, 2)
    # Incorrect dimensions should raise ValueError
    with pytest.raises(ValueError):
        validate_array_shape(arr1, 2)
