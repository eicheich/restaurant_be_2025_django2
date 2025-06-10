import os
import sys

# Add your project directory to the sys.path
sys.path.insert(0, os.path.dirname(__file__))

# Set Django settings module for production
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_be_2025_django.settings_production')

# Import Django and setup
import django
django.setup()

# Import WSGI application
from restaurant_be_2025_django.wsgi import application

# cPanel-specific WSGI configuration
# Path akan otomatis di-set oleh cPanel Python App
# Jika ada error, uncomment dan sesuaikan path berikut:
# INTERP = os.path.expanduser("~/virtualenv/restaurant_be_2025_django/3.10/bin/python")
# if sys.executable != INTERP:
#     os.execl(INTERP, INTERP, *sys.argv)
