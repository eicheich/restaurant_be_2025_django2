#!/usr/bin/env python
"""
Test passenger_wsgi.py configuration
Run this in cPanel terminal to check if WSGI file works
"""
import os
import sys

print("=== Testing passenger_wsgi.py ===")
print("")

try:
    # Test import passenger_wsgi
    sys.path.insert(0, os.path.dirname(__file__))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_be_2025_django.settings_production')

    import django
    django.setup()

    from restaurant_be_2025_django.wsgi import application

    print("✅ passenger_wsgi.py configuration is CORRECT!")
    print("✅ Django application imported successfully")
    print("✅ Production settings loaded")
    print("")
    print("If you still get 'This site can't be reached', check:")
    print("1. Python App status in cPanel (should be Running)")
    print("2. Application Root path in cPanel")
    print("3. Application URL in cPanel")
    print("4. Domain in ALLOWED_HOSTS")

except Exception as e:
    print("❌ passenger_wsgi.py has issues!")
    print(f"Error: {e}")
    print("")
    print("Fix the error above before deploying.")
