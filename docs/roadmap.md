# Neuro Data Engine Roadmap

This roadmap outlines planned improvements and features for upcoming
releases of the Neuro Data Engine.  Dates are indicative and may
change based on contributor availability and user feedback.

## v0.2 (Q3 2026)

* **Configuration merging** – Provide a utility to merge experiment‑specific
  YAML configurations with the base configuration automatically.
* **Additional file loaders** – Add support for HDF5 and NWB (Neurodata Without Borders) formats.
* **Interactive visualisations** – Integrate with [Plotly](https://plotly.com/) or [Bokeh](https://bokeh.org/)
  to provide interactive figures in the notebooks.
* **Continuous integration** – Set up GitHub Actions for linting and running the unit tests on every push.

## v0.3 (Q4 2026)

* **Real‑time streaming** – Support streaming data sources (e.g. UDP or WebSocket)
  for online analysis of neural signals.
* **Machine learning integration** – Provide hooks to feed processed data into
  common machine learning frameworks such as PyTorch or scikit‑learn, and
  include example models for spike sorting or pattern classification.
* **Expanded analysis suite** – Implement additional statistical tests
  (e.g. cross‑correlation, coherence) and more sophisticated pattern
  detectors (e.g. burst detection algorithms).

## v1.0 (2027)

* **Cross‑modal support** – Extend the engine to handle other neuroscience
  data types such as fMRI, EEG or behavioural video.  This will require
  new loaders, preprocessing pipelines and analysis routines.
* **Graphical user interface** – Develop a lightweight GUI for configuring
  pipelines, running analyses and visualising results without writing code.
* **Comprehensive documentation** – Publish a user guide and API
  reference, including tutorials and best practices.

If you would like to contribute to any of these milestones or propose
additional features, please open an issue on the project repository.
