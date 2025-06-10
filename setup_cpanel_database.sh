#!/bin/bash
# Setup script for cPanel MySQL database

echo "=========================================="
echo "cPanel Database Setup Helper"
echo "=========================================="

echo ""
echo "MANUAL STEPS TO COMPLETE IN cPANEL:"
echo "1. Login to your cPanel account"
echo "2. Go to 'MySQL Databases' section"
echo "3. Create a new database named: restaurant_db"
echo "4. Create a new MySQL user with username: restaurant_user"
echo "5. Set a strong password for the user"
echo "6. Add the user to the database with ALL PRIVILEGES"
echo ""

echo "THEN UPDATE settings_production.py with these values:"
echo "Replace these placeholders:"
echo "  'cpanelusername_restaurant_db' -> 'cpanelusername_restaurant_db'"
echo "  'cpanelusername_restaurant_user' -> 'cpanelusername_restaurant_user'"
echo "  'your_database_password' -> 'actual_password'"
echo "  'yourdomain.com' -> 'actual_domain.com'"
echo ""

echo "After setting up the database, run these commands in order:"
echo ""
echo "# 1. Test database connection"
echo "python debug_database.py"
echo ""
echo "# 2. Create and apply migrations (if needed)"
echo "python manage.py makemigrations"
echo "python manage.py migrate"
echo ""
echo "# 3. If migrations fail, try fresh migration"
echo "python manage.py migrate --fake-initial"
echo ""
echo "# 4. Create superuser"
echo "python manage.py createsuperuser"
echo ""
echo "# 5. Collect static files"
echo "python manage.py collectstatic --noinput"
echo ""
echo "# 6. Populate initial data"
echo "python manage.py shell < populate_data.py"
echo ""

# Create a quick settings checker
cat << 'EOF' > check_settings.py
#!/usr/bin/env python
"""
Quick settings checker for production deployment
"""
import os
import sys

# Add project to path
sys.path.append('/home/cpanelusername/restaurant_be_2025_django')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_be_2025_django.settings_production')

import django
django.setup()

from django.conf import settings

print("Current Production Settings:")
print(f"DEBUG: {settings.DEBUG}")
print(f"ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")

db = settings.DATABASES['default']
print(f"\nDatabase Settings:")
print(f"ENGINE: {db['ENGINE']}")
print(f"NAME: {db['NAME']}")
print(f"USER: {db['USER']}")
print(f"HOST: {db['HOST']}")
print(f"PORT: {db['PORT']}")

print(f"\nStatic Files:")
print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
print(f"MEDIA_ROOT: {settings.MEDIA_ROOT}")

# Check if placeholder values are still there
issues = []
if 'yourdomain.com' in str(settings.ALLOWED_HOSTS):
    issues.append("ALLOWED_HOSTS still contains placeholder 'yourdomain.com'")

if 'cpanelusername_' in db['NAME']:
    issues.append("Database NAME still contains placeholder 'cpanelusername_'")

if 'your_database_password' in db['PASSWORD']:
    issues.append("Database PASSWORD still contains placeholder")

if issues:
    print(f"\n⚠️  ISSUES FOUND:")
    for issue in issues:
        print(f"   - {issue}")
    print(f"\nPlease update settings_production.py with actual values")
else:
    print(f"\n✅ Settings look good!")
EOF

chmod +x check_settings.py

echo "Created check_settings.py - run this to verify your production settings"
echo ""
echo "=========================================="
echo "Next: Update settings_production.py, then run debug_database.py"
echo "=========================================="
