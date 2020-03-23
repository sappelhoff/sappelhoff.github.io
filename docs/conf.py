"""Configure details for documentation with sphinx."""
from datetime import date

import sphinx_bootstrap_theme


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages'
]

html_baseurl = 'http://stefanappelhoff.com'

# General information about the project.
project = ''
author = 'Stefan Appelhoff'
year = '2020'
td = date.today()
if year != str(td.year):
    year = '{}-{}'.format(year, td.year)

copyright = '{}, Stefan Appelhoff. Last updated {}'.format(year, td.isoformat())

html_show_sphinx = False  # do not show "created using Sphinx X.Y"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''

# The full version, including alpha/beta/rc tags.
release = version

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# HTML options (e.g., theme)
# see: https://sphinx-bootstrap-theme.readthedocs.io/en/latest/README.html
# Clean up sidebar: Do not show "Source" link
html_show_sourcelink = False

html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

templates_path = ['templates']

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'navbar_title': '',
    'bootswatch_theme': "flatly",
    'navbar_sidebarrel': False,  # no "previous / next" navigation
    'navbar_pagenav': False,  # no "Page" navigation in sidebar
    'bootstrap_version': "3",
    'navbar_links': [
        ("GitHub", "https://github.com/sappelhoff/", True),
        ("Twitter", "https://twitter.com/stefanappelhoff", True),
        ("SoundCloud", "https://soundcloud.com/stefan-appelhoff", True),
        ("Google Scholar", "https://scholar.google.de/citations?user=ceECtQIAAAAJ&hl=en", True),  # noqa: E501
    ]}
