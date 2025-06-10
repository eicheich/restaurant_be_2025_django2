#!/bin/bash

# Script setup untuk deployment Django di cPanel
# Jalankan script ini di terminal cPanel setelah git clone

echo "=== Django cPanel Setup Script ==="

# 1. Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# 2. Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --settings=restaurant_be_2025_django.settings_production

# 3. Run migrations
echo "Running database migrations..."
python manage.py migrate --settings=restaurant_be_2025_django.settings_production

# 4. Create superuser (optional)
echo "Creating superuser... (Anda bisa skip ini jika sudah ada)"
python manage.py createsuperuser --settings=restaurant_be_2025_django.settings_production

# 5. Seed database with initial data
echo "Seeding database with initial data..."
python manage.py seed_db --settings=restaurant_be_2025_django.settings_production

echo "=== Setup completed! ==="
echo "Pastikan untuk:"
echo "1. Update settings_production.py dengan database credentials Anda"
echo "2. Update ALLOWED_HOSTS dengan domain Anda"
echo "3. Restart Python app di cPanel"
