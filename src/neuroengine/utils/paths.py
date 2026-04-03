"""
Path utilities for the Neuro Data Engine.

These helpers build absolute paths to the project's data and results
directories relative to the package root.  When installing as a
package, the root is inferred from the location of this file.
"""

from pathlib import Path
from typing import Optional


# Compute the project root by navigating up from this file:
# src/neuroengine/utils/paths.py -> src/neuroengine/utils -> src/neuroengine -> src -> project root
ROOT = Path(__file__).resolve().parents[3]


def get_data_path(stage: str = "raw") -> Path:
    """Return the absolute path to a data subdirectory.

    Parameters
    ----------
    stage : str, optional
        One of ``raw``, ``interim`` or ``processed``.  The default
        returns the `raw` directory.

    Returns
    -------
    pathlib.Path
        Absolute path to the requested data directory.
    """
    if stage not in {"raw", "interim", "processed"}:
        raise ValueError("stage must be one of 'raw', 'interim' or 'processed'")
    return ROOT / "data" / stage


def get_results_path(subdir: Optional[str] = None) -> Path:
    """Return the absolute path to a subdirectory under `results`.

    Parameters
    ----------
    subdir : str, optional
        Subdirectory name (e.g. ``figures``, ``arrays``, ``reports``).  If
        None, the path to the `results` directory itself is returned.

    Returns
    -------
    pathlib.Path
        Absolute path to the requested results directory.
    """
    base = ROOT / "results"
    return base / subdir if subdir is not None else base
