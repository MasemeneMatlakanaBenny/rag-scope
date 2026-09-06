# Configuration file for the Sphinx documentation builder.

import sys
from pathlib import Path


# The documentation lives in ``docs/`` and the package lives in ``src/``.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / 'src'))


# -- Project information -----------------------------------------------------

project = 'ragscope'
copyright = '2026, Masemene Matlakana Benny'
author = 'Masemene Matlakana Benny'
release = 'v0.1.0'


# -- General configuration ---------------------------------------------------

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
toc_object_entries_show_parents = 'hide'

# API pages describe the public surface and do not execute drift calculations.
autodoc_mock_imports = ['bertopic', 'numpy', 'pandas', 'scipy', 'sklearn']

templates_path = []
exclude_patterns = ['build']


# -- Options for HTML output -------------------------------------------------

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
