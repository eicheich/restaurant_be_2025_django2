#!/bin/bash

# Script khusus untuk fix static files di cPanel
echo "=== Fixing Static Files Issue in cPanel ==="

# Buat direktori yang diperlukan
echo "Creating required directories..."
mkdir -p static
mkdir -p staticfiles
mkdir -p media/images
mkdir -p media/images/menu
mkdir -p media/images/articles

# Buat file .gitkeep untuk memastikan direktori tidak kosong
touch static/.gitkeep
touch staticfiles/.gitkeep
touch media/.gitkeep
touch media/images/.gitkeep

echo "✅ Directories created successfully!"

# Test Django configuration
echo ""
echo "🔍 Testing Django configuration..."
python manage.py check --settings=restaurant_be_2025_django.settings_production

if [ $? -eq 0 ]; then
    echo "✅ Django configuration is valid!"

    # Run migration again
    echo ""
    echo "🗄️ Running migrations..."
    python manage.py migrate --settings=restaurant_be_2025_django.settings_production

    # Collect static files
    echo ""
    echo "📁 Collecting static files..."
    python manage.py collectstatic --noinput --settings=restaurant_be_2025_django.settings_production

    echo ""
    echo "✅ Setup completed successfully!"
    echo ""
    echo "📋 Directory structure created:"
    ls -la static/ staticfiles/ media/

else
    echo "❌ Django configuration has issues. Please check settings_production.py"
fi

echo ""
echo "🔄 Next step: Restart your Python App in cPanel"
