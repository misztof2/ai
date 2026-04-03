"""
Loaders for common data formats used in neuroscience experiments.

The functions in this module provide a thin abstraction over NumPy
and YAML to read data from disk.  Loading routines are intentionally
simple: more sophisticated parsing should be implemented in
experiment‑specific code that calls these functions.
"""

from pathlib import Path
from typing import Any, Dict

import numpy as np
import yaml


def load_csv(path: str | Path, delimiter: str = ",", dtype: Any = float) -> np.ndarray:
    """Load a numeric CSV file into a NumPy array.

    Parameters
    ----------
    path : str or Path
        Path to the CSV file on disk.
    delimiter : str, optional
        Character used to separate values in the file (default is comma).
    dtype : data‑type, optional
        Data type of the resulting array (default is float).

    Returns
    -------
    ndarray
        2D array containing the data from the file.

    Raises
    ------
    FileNotFoundError
        If the specified file does not exist.
    ValueError
        If the file cannot be parsed into a numeric array.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")
    try:
        return np.loadtxt(path, delimiter=delimiter, dtype=dtype)
    except Exception as exc:
        raise ValueError(f"Failed to load CSV file '{path}': {exc}") from exc


def load_numpy(path: str | Path) -> np.ndarray:
    """Load a NumPy binary file (.npy or .npz).

    If the file is an `.npz` archive it returns the first array stored.

    Parameters
    ----------
    path : str or Path
        Path to the `.npy` or `.npz` file.

    Returns
    -------
    ndarray
        NumPy array contained in the file.

    Raises
    ------
    FileNotFoundError
        If the file is not found on disk.
    ValueError
        If the file format is unsupported or cannot be read.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"NumPy file not found: {path}")
    try:
        if path.suffix == ".npz":
            with np.load(path) as data:
                # Return the first array in the archive
                key = next(iter(data.files))
                return data[key]
        else:
            return np.load(path)
    except Exception as exc:
        raise ValueError(f"Failed to load NumPy file '{path}': {exc}") from exc


def load_yaml(path: str | Path) -> Dict[str, Any]:
    """Load a YAML configuration file into a Python dictionary.

    Parameters
    ----------
    path : str or Path
        Path to the YAML file.

    Returns
    -------
    dict
        Parsed configuration as a nested dictionary.

    Raises
    ------
    FileNotFoundError
        If the YAML file cannot be found.
    ValueError
        If the file cannot be parsed as valid YAML.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"YAML file not found: {path}")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as exc:
        raise ValueError(f"Failed to parse YAML file '{path}': {exc}") from exc
