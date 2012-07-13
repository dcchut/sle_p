from pyramid.paster import get_app
application = get_app(
  '/var/www/sleep/live.ini', 'main')
