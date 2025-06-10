#!/bin/bash
# Simple troubleshooting script for cPanel deployment

echo "=== Django cPanel Troubleshooting ==="
echo ""

echo "1. Testing database connection..."
python manage.py check --settings=restaurant_be_2025_django.settings_production
echo ""

echo "2. Checking current migrations..."
python manage.py showmigrations --settings=restaurant_be_2025_django.settings_production
echo ""

echo "3. If no migrations shown above, creating them..."
python manage.py makemigrations api --settings=restaurant_be_2025_django.settings_production
echo ""

echo "4. Running migrations..."
python manage.py migrate --settings=restaurant_be_2025_django.settings_production
echo ""

echo "5. Collecting static files..."
python manage.py collectstatic --noinput --settings=restaurant_be_2025_django.settings_production
echo ""

echo "=== Setup Complete! ==="
echo "Now run: python manage.py createsuperuser --settings=restaurant_be_2025_django.settings_production"
echo "Then run: python manage.py seed_db --settings=restaurant_be_2025_django.settings_production"
