#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Wellston Center'
SITENAME = 'St. Augustine Wellston Center'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

STATIC_PATHS = ['img']

FAVICON = 'img/favicon.ico'
MENUITEMS = [
    ("Home", "index.html"),
    ("About", "about.html"),
    ("Contact", "contact.html")
]
DISPLAY_PAGES_ON_MENU = False

#THEME = 'themes/notmyidea'
THEME = 'themes/twenty'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from utils import filters
JINJA_FILTERS = { 'sidebar': filters.sidebar }

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
