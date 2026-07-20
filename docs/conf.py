# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "DEBrowser"
copyright = "2025, Alper Kucukural, Onur Yukselen, Manuel Garber"
author = "Alper Kucukural, Onur Yukselen, Manuel Garber"
release = "1.31"

# -- General configuration ---------------------------------------------------

extensions = []
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# Prefer the Read the Docs theme when available (installed via
# docs/requirements.txt on RTD); fall back to the built-in alabaster theme so
# local builds work without extra dependencies.
try:
    import sphinx_rtd_theme  # noqa: F401

    html_theme = "sphinx_rtd_theme"
except ImportError:
    html_theme = "alabaster"

html_title = "DEBrowser documentation"
html_static_path = ["_static"]
