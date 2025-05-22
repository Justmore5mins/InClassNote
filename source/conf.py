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
    'sphinx_design'
]


templates_path = ['_templates']
exclude_patterns = ["math/questions.rst"]

language = 'zh-TW'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_permalinks_icon = '<span>#</span>'
html_theme = 'sphinxawesome_theme'
html_title = "上課的筆記"
html_static_path = ['_static']

html_last_updated_fmt = '%B %d, %Y'

html_show_sphinx = False
html_css_files = ["style.css"]
html_js_files = ["script.js"]

from docutils import nodes
from docutils.parsers.rst import roles

def strike_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    node = nodes.raw('', f'<del>{text}</del>', format='html')
    return [node], []

from docutils import nodes
from docutils.parsers.rst import roles

def memes_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Custom :memes:`Shown <link>` role.
    Visible text 'Shown' links to 'link' URL.
    Tooltip shows the link URL.
    """

    if '<' not in text or '>' not in text:
        msg = inliner.reporter.error(
            'Memes role syntax is :memes:`VisibleText <URL>`',
            line=lineno)
        return [], [msg]

    visible, link = text.split('<', 1)
    link = link.rstrip('>')
    visible = visible.strip()
    link = link.strip()

    # Create reference (link) node
    node = nodes.reference(rawtext, visible, refuri=link, classes=['memes-link'])
    node['title'] = link  # tooltip shows URL on hover

    return [node], []

def spoiler_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Custom role: :spoiler:`This is hidden`
    """
    node = nodes.inline(text, text, classes=['spoiler'])
    return [node], []

def setup(app):
    roles.register_local_role('memes', memes_role)
    roles.register_local_role("strike",strike_role)
    roles.register_local_role('beep', spoiler_role)
    app.add_css_file('style.css')
    app.add_js_file('script.js')