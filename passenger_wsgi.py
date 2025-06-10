import os
import sys
import django

# Add your project directory to the sys.path
sys.path.insert(0, os.path.dirname(__file__))

# Set Django settings module for production
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_be_2025_django.settings_production')

# Setup Django
django.setup()

# Import WSGI application
from restaurant_be_2025_django.wsgi import application

# cPanel-specific WSGI configuration
# Ganti path ini dengan path Python environment Anda di cPanel
INTERP = os.path.expanduser("~/virtualenv/restaurant_be_2025_django/3.10/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
