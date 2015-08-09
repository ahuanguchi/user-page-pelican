#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# AUTHOR = 'Alex Huang'
SITENAME = "Alex Huang's Homepage"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
         # ('Python.org', 'http://python.org/'),
         # ('Jinja2', 'http://jinja.pocoo.org/'),
         # ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
          # ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

STATIC_PATHS = [
    'images',
    'extra',
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_RETENTION = ['.git']

DEFAULT_DATE = 'fs'
DISPLAY_CATEGORIES_ON_MENU = False

GITHUB_URL = 'https://github.com/ahuanguchi'

# Cid
THEME = 'theme/Pelican-Cid'
DIRECT_TEMPLATES = [
    'index',
    'archives',
    'categories',
]
SITEFOOTER = 'Built with <a href="http://getpelican.com">Pelican</a> and the <a href="https://github.com/hdra/Pelican-Cid">Cid</a> theme with modifications.'
INDEX_SAVE_AS = 'blog.html'
USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = [
    ('About', 'pages/about.html'),
    ('Projects', 'pages/projects.html'),
    ('Blog', INDEX_SAVE_AS),
]
CONTACTS = [
    ('GitHub', GITHUB_URL),
]
