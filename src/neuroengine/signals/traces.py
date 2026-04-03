"""
Time‑series trace representation.

A `Trace` represents a continuous neural recording sampled at a fixed
rate.  It wraps a NumPy array of data along with metadata such as
sampling rate and optional channel name.  The class exposes convenience
methods to compute basic statistics and to plot the trace.
"""

from dataclasses import dataclass
from typing import Iterable, Optional

import numpy as np
import matplotlib.pyplot as plt


@dataclass
class Trace:
    """A one‑dimensional time‑series with a sampling rate.

    Parameters
    ----------
    data : Iterable[float] or ndarray
        Raw samples of the trace.
    sampling_rate : float
        Sampling rate in Hertz.
    name : str, optional
        Optional identifier for the trace (e.g. channel name).
    """

    data: np.ndarray
    sampling_rate: float
    name: Optional[str] = None

    def __init__(self, data: Iterable[float] | np.ndarray, sampling_rate: float, name: Optional[str] = None) -> None:
        self.data = np.asarray(data, dtype=float)
        self.sampling_rate = float(sampling_rate)
        self.name = name

    def duration(self) -> float:
        """Return the duration of the trace in seconds."""
        return self.data.size / self.sampling_rate

    def mean(self) -> float:
        """Return the mean of the trace."""
        return float(np.mean(self.data))

    def std(self) -> float:
        """Return the standard deviation of the trace."""
        return float(np.std(self.data))

    def plot(self, ax: Optional[plt.Axes] = None, **kwargs) -> plt.Axes:
        """Plot the trace using matplotlib.

        Parameters
        ----------
        ax : matplotlib.axes.Axes, optional
            Existing axes to plot into.  If None, a new figure and axes
            will be created.
        kwargs : dict
            Additional keyword arguments passed to `ax.plot`.

        Returns
        -------
        matplotlib.axes.Axes
            The axes containing the plot.
        """
        if ax is None:
            fig, ax = plt.subplots()
        times = np.arange(self.data.size) / self.sampling_rate
        ax.plot(times, self.data, **kwargs)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Amplitude")
        title = self.name if self.name else "Trace"
        ax.set_title(title)
        return ax
