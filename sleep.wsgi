import os
import sys
import site

site.addsitedir('/var/www/sleep/env/lib/python2.7/site-packages')

from pyramid.paster import get_app
application = get_app(
  '/var/www/sleep/live.ini', 'main')
