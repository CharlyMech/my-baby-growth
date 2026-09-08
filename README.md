# My baby's growth follow up

Data-focused follow up of a baby's growth: recording measurements (weight,
height, head circumference) over time and validating the baby's identification
data.

## Repository contents

| Path | Description |
| --- | --- |
| `main.ipynb` | Interactive flow: loads the list of babies, lets you pick one, creates or reads its growth CSV and records new measurements. |
| `main.py` | CLI interface (pending, `TODO`). |
| `models/baby.py` | Pydantic `Baby` model with birth data (name, date/time, gender, measurements at birth, birth place and type). |
| `models/registry.py` | Pydantic `GrowthRegistry` model: one measurement (`weight_kg`, `height_cm`, `head_circum_cm`, `date`). |
| `utils/files.py` | Reading JSON and CSV, and loading a CSV into a Polars `DataFrame`. |
| `utils/inputs.py` | Console input helpers (positive number, date, datetime). |
| `utils/dates.py` | Date validation (pending). |
| `data/` | Input/output data (see below). |

### Data (`data/`)

- `data/babies.json` — list of babies (one or more), validated against the `Baby` model.
- `data/<baby_id>.csv` — growth records for each baby; created with the first
  measurement (taken from the birth data).
- `*.example.*` files are versioned as templates. Real data (`data/*.json`,
  `data/*.csv`) is ignored by Git.

## Requirements

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or Anaconda (`conda`).
- Python 3.14 (pinned by `environment.yml`).
- Main dependencies: `polars`, `pydantic`, `ipywidgets` (for the notebook's baby
  selector), `jupyter`.

## Initialize the environment with conda

`environment.yml` was generated with `conda env export --from-history`.

```bash
# Create the environment
conda env create -f environment.yml

# Activate it
conda activate my-baby-growth
```

## Update the environment after installing new packages

```bash
# 1. Install the new package in the active environment
conda install -c conda-forge <package>

# 2. Regenerate environment.yml (only explicitly requested dependencies)
conda env export --from-history > environment.yml
```

To apply an already-updated `environment.yml` on another machine:

```bash
conda env update -f environment.yml --prune
```

## Usage

```bash
conda activate my-baby-growth
jupyter notebook main.ipynb
```

1. Copy `data/babies.example.json` to `data/babies.json` and fill in the baby's data.
2. Run the notebook cells in order.
3. If there is more than one baby, pick one from the dropdown and confirm.
4. The first run creates `data/<baby_id>.csv` with the birth measurement;
   later runs let you add new measurements.
