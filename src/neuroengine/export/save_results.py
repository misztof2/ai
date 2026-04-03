"""
Functions for saving results to disk.

These utilities wrap common operations for persisting figures, arrays
and plain‑text reports.  They ensure that parent directories exist
before writing and catch common exceptions.
"""

from pathlib import Path
from typing import Any

import numpy as np


def _ensure_parent_dir(path: Path) -> None:
    """Create parent directories for the given file path if needed."""
    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)


def save_figure(fig: Any, path: str | Path, **kwargs) -> None:
    """Save a matplotlib figure to disk.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Figure object to save.
    path : str or Path
        Destination path, including extension (e.g. `.png` or `.pdf`).
    kwargs : dict
        Additional arguments forwarded to `Figure.savefig`.
    """
    p = Path(path)
    _ensure_parent_dir(p)
    fig.savefig(p, **kwargs)


def save_array(arr: np.ndarray, path: str | Path) -> None:
    """Save a NumPy array to disk as `.npy`.

    Parameters
    ----------
    arr : ndarray
        Array to save.
    path : str or Path
        Destination path.  The file will be saved in NumPy's binary
        format (`.npy`).
    """
    p = Path(path)
    _ensure_parent_dir(p)
    np.save(p, arr)


def save_report(text: str, path: str | Path) -> None:
    """Write a plain‑text report to disk.

    Parameters
    ----------
    text : str
        Text to write to the report file.
    path : str or Path
        Destination path.  Parent directories will be created if they
        do not exist.
    """
    p = Path(path)
    _ensure_parent_dir(p)
    with open(p, "w", encoding="utf-8") as f:
        f.write(text)
