# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
from pathlib import Path


# Make the package available to autodoc without requiring a prior installation.
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / 'src'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ragscope'
copyright = '2026, Masemene Matlakana Benny'
author = 'Masemene Matlakana Benny'
release = 'v0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
]

autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'show-inheritance': False,
}
autodoc_typehints = 'description'
# Keep the page-level API navigation concise: show ``method()`` rather than
# the fully qualified ``ClassName.method()`` for entries inside a class.
toc_object_entries_show_parents = 'hide'
# API pages describe the public surface and do not execute drift calculations.
# Mock runtime-only libraries so a documentation-only environment can build them.
autodoc_mock_imports = ['bertopic', 'numpy', 'pandas', 'scipy', 'sklearn']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_theme_options = {
    'logo': {'text': 'RAGScope'},
    'navbar_start': ['navbar-logo'],
    'navbar_center': ['navbar-nav'],
    'navbar_end': ['theme-switcher', 'navbar-icon-links'],
    'secondary_sidebar_items': ['page-toc'],
    'show_nav_level': 2,
    'show_toc_level': 2,
    'show_prev_next': False,
}
