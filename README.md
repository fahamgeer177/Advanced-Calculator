# Advanced Calculator

Advanced Calculator is a Python project with two interfaces:

- CLI calculator with Simple and Scientific modes
- GUI calculator built with PyQt5

It supports common arithmetic, scientific operations, input validation, and operation history logging.

## Features

- Two modes: Simple and Scientific
- CLI mode switching during runtime
- GUI mode switching with dedicated button layouts
- Scientific functions: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `log`, `log10`, `sqrt`, `exp`, factorial
- Constants: `pi`, `e`
- Error handling for invalid input and division by zero
- Operation history saved to `calc_history.log` (CLI)

## Project Structure

```text
.
|- app.py          # PyQt5 GUI entry point
|- calculator.py   # Calculator logic + CLI entry point
|- setup.py        # Packaging metadata and console entry point
|- README.md
```

## Requirements

- Python 3.8+
- `colorama`
- `PyQt5` (required for GUI)

Install dependencies:

```bash
pip install colorama PyQt5
```

## Run the App

CLI (simple mode):

```bash
python calculator.py --mode simple
```

CLI (scientific mode):

```bash
python calculator.py --mode scientific
```

GUI:

```bash
python app.py
```

## Optional: Install as a Command

You can install the project locally and use the console script from `setup.py`:

```bash
pip install -e .
advanced-calculator
```

## GitHub Push Guide

If this is your first push for this project:

```bash
git init
git branch -M main
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

If the remote already exists:

```bash
git push
```

## Notes

- `__pycache__/` and log files should not be tracked in git.
- Add screenshots in this README once you capture CLI/GUI output.
