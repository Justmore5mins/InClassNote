# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import datetime

project = 'InClassNote'
copyright = '2025, Justmore5mins'
author = 'Justmore5mins'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx_tabs.tabs',
    'sphinxawesome_theme',
    'sphinx_design',
]

templates_path = ['_templates']
exclude_patterns = ["math/questions.rst"]

language = 'zh-tw'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'
html_title = "上課的筆記"
html_static_path = ['_static']
html_css_file = ['style.css']

html_last_updated_fmt = '%B %d, %Y'

html_show_sphinx = False

from docutils import nodes
from docutils.parsers.rst import roles

def strike_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.raw('', f'<del>{text}</del>', format='html')
    return [node], []

roles.register_local_role('strike', strike_role)