#!/bin/bash

# Script untuk setup database di cPanel
# Pastikan sudah update settings_production.py dengan database credentials yang benar

echo "=== Setting up Django Database ==="

# Run migrations
echo "Running database migrations..."
python manage.py migrate --settings=restaurant_be_2025_django.settings_production

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --settings=restaurant_be_2025_django.settings_production

# Create superuser (akan prompt untuk input)
echo "Creating superuser account..."
python manage.py createsuperuser --settings=restaurant_be_2025_django.settings_production

# Seed database with initial data
echo "Seeding database with initial data..."
python manage.py seed_db --settings=restaurant_be_2025_django.settings_production

echo "=== Database setup completed! ==="
echo ""
echo "Final steps:"
echo "1. Restart Python App di cPanel"
echo "2. Test API di: https://yourdomain.com/restaurant-api/api/"
echo "3. Access admin di: https://yourdomain.com/restaurant-api/admin/"
