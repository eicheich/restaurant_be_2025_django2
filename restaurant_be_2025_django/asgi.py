"""
ASGI config for restaurant_be_2025_django project.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_be_2025_django.settings')

application = get_asgi_application()
