# Graphing Calculator Package

Small python library that lets you graph mathematical equations using matplotlib. By passing a standard equation string directly into the `draw_graph` function, the library dynamically parses the math and renders the plot.

A ci/cd pipeline was added. 

---

## Requirements & Dependencies

This library uses the following standard scientific computing packages. They are automatically managed when you install via `pip`, but you can find them listed in `requirements.txt`:

* **Python** `>= 3.10`
* **NumPy** (Array manipulations)
* **SymPy** (Symbolic math evaluation)
* **Matplotlib** (Graph rendering)
* **Pytest & Pytest-Cov** (Development & testing)

---

## Installation

You can install this package directly from the public Python Package Index (PyPI) using `pip`:

```bash
pip install diego_m_calculator