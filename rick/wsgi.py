"""
WSGI config for www project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
import os
from os.path import dirname
import sys

from django.core.wsgi import get_wsgi_application

PROJECT_DIR = dirname(dirname(os.path.abspath(__file__)))

sys.path.insert(0, PROJECT_DIR)
print(PROJECT_DIR)
print(sys)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rick.settings')

application = get_wsgi_application()
