"""
Validation utilities for input data structures.

These helpers check that arrays conform to expected dimensions and types.
Raising exceptions early helps catch data issues before downstream processing.
"""

import numpy as np


def validate_array_shape(arr: np.ndarray, ndim: int) -> None:
    """Validate that a NumPy array has a given number of dimensions.

    Parameters
    ----------
    arr : ndarray
        Array to validate.
    ndim : int
        Expected number of dimensions (e.g. 1 for a single trace, 2 for
        multiple traces in rows or columns).

    Raises
    ------
    TypeError
        If `arr` is not a NumPy array.
    ValueError
        If the array does not have the expected dimensionality.
    """
    if not isinstance(arr, np.ndarray):
        raise TypeError(f"Expected a NumPy array, got {type(arr)!r}")
    if arr.ndim != ndim:
        raise ValueError(
            f"Expected array with {ndim} dimensions, got {arr.ndim} dimensions"
        )
