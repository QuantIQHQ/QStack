"""
WSGI config for quantiq_demo_project project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quantiq_demo_project.settings')

application = get_wsgi_application()