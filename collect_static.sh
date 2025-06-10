#!/bin/bash

# Script untuk collect static files di cPanel
echo "=== Collecting Static Files ==="

# Buat direktori jika belum ada
mkdir -p static
mkdir -p staticfiles
mkdir -p media/images

# Collect static files
python manage.py collectstatic --noinput --settings=restaurant_be_2025_django.settings_production

echo "=== Static files collected successfully! ==="
echo "Files location:"
echo "- Static files: ./staticfiles/"
echo "- Media files: ./media/"
