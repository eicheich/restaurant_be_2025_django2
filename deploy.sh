#!/bin/bash

# Django Restaurant API - GitHub + cPanel Deployment Script
# Run this script after cloning from GitHub to cPanel

echo "🚀 Starting Django Restaurant API deployment from GitHub..."

# Pull latest changes from GitHub
echo "📥 Pulling latest changes from GitHub..."
git pull origin main

# Set environment variables
export DJANGO_SETTINGS_MODULE="restaurant_be_2025_django.settings_production"

# Activate virtual environment (adjust path as needed)
echo "🐍 Activating virtual environment..."
source ~/virtualenv/restaurant_api/3.*/bin/activate

# Install/update dependencies
echo "📦 Installing/updating Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Database migrations
echo "🗄️ Running database migrations..."
python manage.py makemigrations --settings=restaurant_be_2025_django.settings_production
python manage.py migrate --settings=restaurant_be_2025_django.settings_production

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput --settings=restaurant_be_2025_django.settings_production

# Load sample data (optional - only for first deployment)
if [ "$1" = "--with-data" ]; then
    echo "🌱 Loading sample data..."
    python manage.py seed_db --settings=restaurant_be_2025_django.settings_production
fi

# Restart Python application
echo "🔄 Restarting Python application..."
mkdir -p tmp
touch tmp/restart.txt

echo "✅ Deployment completed successfully!"
echo "🔗 Your API is ready at: https://yourdomain.com/api/"
echo ""
echo "📋 Usage:"
echo "  ./deploy.sh               # Regular deployment"
echo "  ./deploy.sh --with-data   # First deployment with sample data"
echo ""
echo "🧪 Test endpoints:"
echo "  https://yourdomain.com/api/categories/"
echo "  https://yourdomain.com/api/menu-items/"
echo "  https://yourdomain.com/api/articles/"
echo "  https://yourdomain.com/admin/"
