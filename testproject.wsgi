import os
import sys	
sys.path.append('/var/www/html/')
sys.path.append('/var/www/html/testproject')
os.environ['DJANGO_SETTINGS_MODULE'] = 'testprojectSettings.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()