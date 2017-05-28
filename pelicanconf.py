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
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

PLUGIN_PATHS = ['pelican-plugins', 'plugins']
# Pelican plugins:
PLUGINS = [  # These plugins are part of the official `pelican-plugins` repo:
           'render_math',
           'summary',
           'neighbors',
           # This one is a custom plugin:
           # 'pdf',
           ]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('github', 'https://tobymccann.github.com/'),)

# Social widget
SOCIAL = (('twitter', '@tobymccann'),
          ('instagram', '@tobymccann'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

OUTPUT_RETENTION = [".git"]