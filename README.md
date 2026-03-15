# Advanced Calculator 🧮

Build fast calculations in both terminal and desktop UI with one Python project.

## ✨ Overview

Advanced Calculator includes two interfaces:

- 💻 CLI calculator with Simple and Scientific modes
- 🖼️ GUI calculator built with PyQt5

It supports arithmetic, scientific operations, input validation, and history logging.

## 🚀 Features

- 🔁 Dual modes: Simple and Scientific
- 🎛️ Runtime mode switching in CLI
- 🧭 Mode switcher and dedicated layouts in GUI
- 🧠 Scientific functions: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `log`, `log10`, `sqrt`, `exp`, factorial
- 📐 Constants: `pi`, `e`
- 🛡️ Error handling for invalid input and division by zero
- 📝 Operation history saved to `calc_history.log` (CLI)

## 📁 Project Structure

```text
.
|- app.py          # PyQt5 GUI entry point
|- calculator.py   # Calculator logic + CLI entry point
|- setup.py        # Packaging metadata and console entry point
|- README.md
```

## 📦 Requirements

- Python 3.8+
- `colorama`
- `PyQt5` (required for GUI)

Install dependencies:

```bash
pip install colorama PyQt5
```

## ▶️ Run the App

CLI (Simple mode):

```bash
python calculator.py --mode simple
```

CLI (Scientific mode):

```bash
python calculator.py --mode scientific
```

GUI:

```bash
python app.py
```

## ⚙️ Optional: Install as a Command

You can install the project locally and use the console script from `setup.py`:

```bash
pip install -e .
advanced-calculator
```

## 🖼️ Screenshots

### Simple Mode

![Simple Mode](simple.png)

### Scientific Mode

![Scientific Mode](scientific.png)

## 📌 Notes

- ✅ `__pycache__/` and log files should not be tracked in git.
- 📸 Add screenshots in this README once you capture CLI/GUI output.
