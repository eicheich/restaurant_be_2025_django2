from restaurant_be_2025_django.wsgi import application
import os
import sys

# cPanel-specific WSGI configuration
INTERP = os.path.expanduser("/home/houselab/virtualenv/restaurant_be_2025_django/3.10/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# The application variable will be used by the server
