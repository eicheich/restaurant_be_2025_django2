#!/bin/bash
# Simple setup script for cPanel deployment

echo "=== Django Restaurant API Setup ==="

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser (optional)
echo "Creating superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else None" | python manage.py shell

# Seed database with sample data (optional)
echo "Seeding database..."
python manage.py seed_db

echo "=== Setup Complete ==="
echo "Your API is ready at: /api/menu-categories/"
