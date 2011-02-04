import os, sys
sys.path.append('/var/www/thodol')
os.environ['DJANGO_SETTINGS_MODULE'] = 'thodol.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()