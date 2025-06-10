"""
WSGI config for restaurant_be_2025_django project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_be_2025_django.settings')

application = get_wsgi_application()
