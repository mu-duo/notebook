# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'rergession-system-doc'
copyright = '2024, tanlinfeng'
author = 'tanlinfeng'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxcontrib.mermaid',
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

themes = [
    "alabaster",     # 0
    "classic",       # 1
    "sphinxdoc",     # 2
    "scrolls",       # 3
    "agogo",         # 4
    "traditional",   # 5
    "nature",        # 6
    "haiku",         # 7
    "pyramid",       # 8
    "bizstyle",      # 9
]
# 推荐 4, 6, 8
html_theme = themes[8]

# required sphinx-rtd-theme
html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]
html_css_files = [
    "custom.css"
]
