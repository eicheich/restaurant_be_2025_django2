#!/bin/bash

# Django Restaurant API - Deployment Script for cPanel
# Run this script after uploading files to cPanel

echo "🚀 Starting Django Restaurant API deployment..."

# Set environment variables
export DJANGO_SETTINGS_MODULE="restaurant_be_2025_django.settings_production"

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Database migrations
echo "🗄️ Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Load sample data (optional)
echo "🌱 Loading sample data..."
python manage.py seed_db

echo "✅ Deployment completed successfully!"
echo "🔗 Your API is ready at: https://yourdomain.com/api/"
echo ""
echo "📋 Next steps:"
echo "1. Update ALLOWED_HOSTS in settings_production.py with your domain"
echo "2. Update database credentials in settings_production.py"
echo "3. Create superuser: python manage.py createsuperuser"
echo "4. Test API endpoints"
