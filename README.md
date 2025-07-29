# Bonan Modeling Python

Python translation of Gordon Bonan's modeling code from the book:
**"Climate Change and Terrestrial Ecosystem Modeling"** (Cambridge University Press, 2019)

Original Fortran/C code repository: [gbonan/bonanmodeling](https://github.com/gbonan/bonanmodeling)

## 📘 Book Information
- Title: Climate Change and Terrestrial Ecosystem Modeling
- Author: Gordon Bonan (NCAR)
- DOI: [10.1017/9781107339217](https://doi.org/10.1017/9781107339217)
- Publisher: Cambridge University Press

## 🌱 Project Goal

This repository provides a Python implementation of ecosystem and climate models from the textbook, making it easier to understand, modify, and extend for research and education.

## 📂 Structure

- `bonanmodel/` – Core Python modules implementing radiation, photosynthesis, soil water balance, and energy models.
- `notebooks/` – Jupyter notebooks demonstrating model usage and simulations.
- `data/` – Sample meteorological and vegetation data for testing.
- `tests/` – Unit tests to validate implementation accuracy.

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/bonanmodeling-python.git
cd bonanmodeling-python
pip install -r requirements.txt
````

## 📊 Example

```python
from bonanmodel import radiation

Q_in = 1360  # W/m² incoming solar radiation
albedo = 0.23
Q_absorbed = radiation.net_radiation(Q_in, albedo)

print(f"Net radiation absorbed: {Q_absorbed} W/m²")
```

## 📜 License

MIT License

## 🧪 Tests

```bash
pytest tests/
```

## ✍️ Credits

Python port by \[Your Name]. Original models by Gordon Bonan.

### ⚠️ Disclaimer

This repository is a **Python rewrite** based on the **MATLAB code** that accompanies the book *Climate Change and Terrestrial Ecosystem Modeling* by Gordon Bonan. It is intended solely for **educational and research purposes**.

* This project **does not claim any copyright** over the original code, book content, or scientific models.
* All credit for the original modeling framework goes to **Gordon Bonan** and the associated authors.
* This Python version is independently developed to help **Python users** access and understand the models.
* If you use or adapt this code, please also cite the original book and code repository:

> Bonan, G. B. (2019). *Climate Change and Terrestrial Ecosystem Modeling*. Cambridge University Press.
> [https://doi.org/10.1017/9781107339217](https://doi.org/10.1017/9781107339217)

