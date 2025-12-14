"""
WSGI config for debye project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

project_path = '/home/Adorik/debye'
if project_path not in sys.path:
    sys.path.append(project_path)

from django.core.wsgi import get_wsgi_application

os.environ.('DJANGO_SETTINGS_MODULE') = 'debye.settings'

application = get_wsgi_application()
