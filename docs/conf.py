# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os

from importlib import metadata

PACKAGE_VERSION = metadata.version('robopanda')
version = release = PACKAGE_VERSION

project = 'robopanda'
copyright = '2023, Sam Maule'
author = 'Sam Maule'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autodoc.typehints',
]
autodoc_mock_imports = ['pandas']
nitpick_ignore = [('py:class', 'pandas.DataFrame')]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Setup for sphinx-apidoc -------------------------------------------------

# Read the Docs doesn't support running arbitrary commands like tox.
# sphinx-apidoc needs to be called manually if Sphinx is running there.
# https://github.com/readthedocs/readthedocs.org/issues/1139

if os.environ.get("READTHEDOCS") == "True":
    from pathlib import Path

    PROJECT_ROOT = Path(__file__).parent.parent
    PACKAGE_ROOT = PROJECT_ROOT / "src" / "imppkg"

    def run_apidoc(_):
        from sphinx.ext import apidoc
        apidoc.main([
            "--force",
            "--implicit-namespaces",
            "--module-first",
            "--separate",
            "-o",
            str(PROJECT_ROOT / "docs" / "reference"),
            str(PACKAGE_ROOT),
            str(PACKAGE_ROOT / "*.c"),
            str(PACKAGE_ROOT / "*.so"),
        ])

    def setup(app):
        app.connect('builder-inited', run_apidoc)