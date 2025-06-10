#!/bin/bash

# Script untuk install dependencies di cPanel
# Jalankan di terminal cPanel setelah membuat Python App

echo "=== Installing Django Restaurant API Dependencies ==="

# Install all required packages
pip install Django==4.2.10
pip install djangorestframework==3.14.0
pip install django-cors-headers==4.3.1
pip install Pillow==10.0.1
pip install mysqlclient==2.2.1
pip install python-slugify==8.0.1
pip install gunicorn==21.2.0
pip install dj-database-url==2.1.0
pip install PyMySQL==1.1.1

echo "=== Dependencies installed successfully! ==="
echo ""
echo "Next steps:"
echo "1. Update settings_production.py dengan database credentials Anda"
echo "2. Update ALLOWED_HOSTS dengan domain Anda"
echo "3. Jalankan script setup_database.sh untuk setup database"
