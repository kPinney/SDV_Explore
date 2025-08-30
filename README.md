# SDV Exploratory Project

## Purpose

This project is an exploratory setup for the Synthetic Data Vault (SDV) library. It provides a well-structured and maintainable foundation for generating synthetic data, making it easy to build upon and share with others.

## Project Structure

```
├── data/
│   └── sample_data.csv
├── metadata/
├── notebooks/
│   └── sdv_exploration.ipynb
├── reports/
├── src/
│   ├── constraints.py
│   ├── data_loader.py
│   ├── selection.py
│   ├── synthesizer.py
│   └── evaluation.py
├── tests/
│   ├── test_constraints.py
│   ├── test_data_loader.py
│   ├── test_evaluation.py
│   └── test_synthesizer.py
├── .gitignore
├── main.py
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Features

*   **Multiple Synthesizers:** Easily switch between `GaussianCopula`, `CTGAN`, and `TVAE` synthesizers.
*   **Automatic Synthesizer Selection:** Automatically selects the best synthesizer for your data based on the quality score.
*   **Data Constraints:** Define constraints to enforce data integrity rules.
*   **Comprehensive Evaluation:** Generate quality reports, plot column distributions, compare correlation matrices, and visualize PCA plots.

## Setup and Installation

### Using Poetry

1.  **Install Poetry:** If you don't have Poetry, follow the instructions on the [official website](https://python-poetry.org/docs/#installation).
2.  **Install dependencies:**
    ```bash
    poetry install
    ```

### Using Pip

1.  **Create a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## How to Run

The `main.py` script is configured to automatically select the best synthesizer and generate evaluation plots.

```bash
python main.py
```

This will:
1.  Load the data from `data/sample_data.csv`.
2.  Iterate through the available synthesizers and evaluate each one.
3.  Print the name of the best synthesizer and its quality score.
4.  Save column distribution plots for the best synthetic data to the `reports/` directory.

## Testing

To run the tests, use `pytest` from the root directory:

```bash
pytest
```
