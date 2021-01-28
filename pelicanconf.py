#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'GLUG-NITH'
SITENAME = 'GNU/Linux Users Group NITH'
SITEURL = ''

THEME = 'themes/alchemy'
THEME_CSS_OVERRIDES = 'themes/bootstrap.min.css'
PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL Flexibility
ARTICLE_URL = 'posts/{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = PAGE_URL

# icons
ICONS = [
    ('github', "https://github.com/glugnith"),
    ('instagram', 'https://www.instagram.com/glugnith')
]

DEFAULT_PAGINATION = 10
PYGMENTS_STYLE = 'monokai'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True