# Neuro Data Engine Architecture

This document describes the architecture of the Neuro Data Engine and
explains how its components interact.  The engine is designed around a
simple **data pipeline** concept: raw recordings are ingested from disk,
preprocessed to remove artefacts, represented in convenient data
structures, analysed to extract meaningful metrics, visualised and
finally exported.  Each stage is implemented in its own module to
promote reuse and modularity.

## Layers of the engine

The engine is organised into the following functional layers:

1. **I/O (`src/neuroengine/io`)** – Responsible for loading data from
   common file formats (CSV, NumPy, YAML).  This layer also performs
   basic validation of array shapes and data types to ensure that
   subsequent steps operate on consistent inputs.

2. **Preprocessing (`src/neuroengine/preprocess`)** – Implements routines
   to clean raw signals.  Currently the engine supports:
   * **Baseline correction** – subtracts a moving average to remove slow
     drifts using `baseline_correction()`.
   * **Normalisation** – rescales signals via z‑score or min–max
     normalisation (`zscore_normalization()`, `minmax_normalization()`).
   * **Filtering** – wraps SciPy’s Butterworth filters to provide
     low‑pass and high‑pass filters (`lowpass_filter()`, `highpass_filter()`).

3. **Signals (`src/neuroengine/signals`)** – Defines abstractions for
   working with continuous recordings.  The `Trace` class stores a
   time‑series along with its sampling rate and provides methods to
   compute duration, mean and standard deviation as well as a built‑in
   plotting method.

4. **Analysis (`src/neuroengine/analysis`)** – Contains statistical
   functions and simple pattern detection.  Examples include `mean()` and
   `variance()` wrappers around NumPy, `autocorrelation()` for
   autocorrelation coefficients and `detect_peaks()` to find threshold
   crossings in a signal.

5. **Visualisation (`src/neuroengine/visualization`)** – Provides
   thin wrappers around matplotlib for plotting traces and histograms.
   These helpers set sensible axis labels and titles and return axes to
   allow further customisation.

6. **Export (`src/neuroengine/export`)** – Implements functions to
   persist results such as figures, arrays and text reports to disk.
   The export layer ensures that parent directories exist and handles
   both absolute and relative paths.

7. **Utils (`src/neuroengine/utils`)** – Supplies miscellaneous helpers
   used across the engine.  For example, `paths.py` constructs paths
   relative to the project root, making the code resilient to changes in
   working directory.

```
           +-------------+      +---------------+      +-------------+
           |   raw data   | --> |  preprocessing | --> |   analysis  |
           +-------------+      +---------------+      +-------------+
                  |                    |                     |
                  v                    v                     v
           +-------------+      +---------------+      +-------------+
           |     I/O     | --> |    signals    | --> | visualization |
           +-------------+      +---------------+      +-------------+
                  |                                           |
                  v                                           v
           +-------------+                               +-------------+
           |   configs   |                               |    export   |
           +-------------+                               +-------------+
```

The ASCII diagram above illustrates the flow of data through the engine.
Configuration settings (top right) influence preprocessing and analysis
behaviour.  Processed signals can be visualised at any stage, and
results are persisted via the export layer.

## Configuration system

The engine reads YAML configuration files from the `configs/`
directory.  A base configuration (`base.yaml`) defines global default
parameters such as sampling rate, baseline window length and filter
cutoff frequency.  Experiment‑specific configurations (e.g. for calcium
imaging) live in subdirectories and may override base values.  Use the
`extends` key to indicate inheritance:

```yaml
extends: base
dataset:
  sampling_rate: 10.0
preprocess:
  baseline_window: 50
```

When loading a configuration with `io.load_yaml()` you can merge it
with the base configuration manually to obtain a complete set of
parameters.

## Extending the engine

The modular architecture makes it straightforward to add new
functionality.  To support a new file format, implement a loader
function in `src/neuroengine/io/loaders.py`.  To add a new pre‑ or
post‑processing step, create a function or module under
`src/neuroengine/preprocess` or `src/neuroengine/analysis` and expose
it in the corresponding `__init__.py`.  Likewise, new visualisation
routines belong under `src/neuroengine/visualization` and should
generate plots using matplotlib.

Unit tests in the `tests/` directory ensure that core functionality
remains intact as you extend the engine.  Please add tests for new
features and run them regularly using `pytest` to maintain stability.
