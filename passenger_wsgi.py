import os
import sys

# Add project to path
sys.path.insert(0, os.path.dirname(__file__))

# Set settings for production
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_be_2025_django.settings_production')

# Setup Django
import django
django.setup()

# Get WSGI application
from restaurant_be_2025_django.wsgi import application
