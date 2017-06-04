#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jason Kennemer'
SITENAME = 'network dev'
SITEURL = ''

PATH = 'content'
THEME = 'themes/pelican-alchemy/alchemy'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'en'
# Extract a post's date from the filename:
#FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
STATIC_PATHS = ['images', 'widgets', 'extra']
EXTRA_PATH_METADATA = {
    'images/favicon.png': {'path': 'favicon.png'},
    'extra/CNAME': {'path': 'CNAME'},
}

PLUGIN_PATHS = ['pelican-plugins', 'plugins']
# Pelican plugins:
PLUGINS = [  # These plugins are part of the official `pelican-plugins` repo:
           'render_math',
           'summary',
           'neighbors',
           'pelican-bootstrapify'
           ]

BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
    'blockquote': ['blockquote'],
}

PYGMENTS_STYLE = 'monokai'

HIDE_AUTHORS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('github', 'https://github.com/tobymccann'),)

# Social widget
SOCIAL = (('twitter', '@tobymccann'),
          ('instagram', '@tobymccann'),)

TWITTER_USERNAME = 'tobymccann'
GITHUB_USERNAME = 'tobymccann'

DEFAULT_PAGINATION = 10

GOOGLE_ANALYTICS = "UA-60159990-3"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

OUTPUT_RETENTION = [".git"]