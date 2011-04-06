'''Retrieve current text from Wordpress.

Uses the https://bitbucket.org/rgrp/pywordpress/src
'''
import os
from pywordpress import Wordpress

w = Wordpress.init_from_config('config.ini')
for p in w.get_page_list():
    p = w.get_page(p['page_id'])
    if not p['wp_slug']:
        continue
    print 'Processing', p['wp_slug'], p['title']
    path = os.path.join('cache', p['wp_slug'] + '.rst')
    heading = len(p['title']) * '='
    text = '%s\n%s\n%s\n\n' % (heading, p['title'], heading) + p['description']
    fo = open(path, 'w')
    text = text.encode('utf8')
    fo.write(text)
    fo.close()

