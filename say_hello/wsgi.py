"""
WSGI config for www project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
from os.path import dirname, abspath

from django.core.wsgi import get_wsgi_application

PROJECT_DIR = dirname(dirname(abspath(__file__)))


sys.path.append("/mysite/say_hello/say_hello")
sys.path.append("/mysite/say_hello")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "say_hello.settings")


application = get_wsgi_application()
