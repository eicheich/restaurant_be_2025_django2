#!/bin/bash

# Complete setup script untuk deployment Django di cPanel
# Jalankan script ini setelah:
# 1. Git clone project ke cPanel
# 2. Setup Python App di cPanel
# 3. Update database credentials di settings_production.py

echo "=========================================="
echo "   Django Restaurant API - cPanel Setup   "
echo "=========================================="

# Step 1: Install Dependencies
echo ""
echo "📦 Step 1: Installing Dependencies..."
pip install -r requirements.txt
if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully!"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Step 2: Check Django Configuration
echo ""
echo "🔍 Step 2: Checking Django Configuration..."
python manage.py check --settings=restaurant_be_2025_django.settings_production
if [ $? -eq 0 ]; then
    echo "✅ Django configuration is valid!"
else
    echo "❌ Django configuration has errors"
    exit 1
fi

# Step 3: Run Database Migrations
echo ""
echo "🗄️ Step 3: Running Database Migrations..."
python manage.py migrate --settings=restaurant_be_2025_django.settings_production
if [ $? -eq 0 ]; then
    echo "✅ Database migrations completed!"
else
    echo "❌ Database migration failed"
    exit 1
fi

# Step 4: Collect Static Files
echo ""
echo "📁 Step 4: Collecting Static Files..."
python manage.py collectstatic --noinput --settings=restaurant_be_2025_django.settings_production
if [ $? -eq 0 ]; then
    echo "✅ Static files collected successfully!"
else
    echo "❌ Static files collection failed"
    exit 1
fi

# Step 5: Create Superuser (Interactive)
echo ""
echo "👤 Step 5: Creating Superuser..."
echo "Please create an admin account:"
python manage.py createsuperuser --settings=restaurant_be_2025_django.settings_production

# Step 6: Seed Database with Initial Data
echo ""
echo "🌱 Step 6: Seeding Database with Initial Data..."
python manage.py seed_db --settings=restaurant_be_2025_django.settings_production
if [ $? -eq 0 ]; then
    echo "✅ Database seeded successfully!"
else
    echo "❌ Database seeding failed"
    exit 1
fi

echo ""
echo "=========================================="
echo "           🎉 Setup Complete!             "
echo "=========================================="
echo ""
echo "✅ Your Django Restaurant API is ready!"
echo ""
echo "📋 Next Steps:"
echo "1. Restart your Python App in cPanel"
echo "2. Test your API at: https://yourdomain.com/restaurant-api/api/"
echo "3. Access admin panel: https://yourdomain.com/restaurant-api/admin/"
echo ""
echo "🔗 Available Endpoints:"
echo "   • Menu Categories: /api/menu/categories/"
echo "   • Menu Items: /api/menu/items/"
echo "   • Articles: /api/articles/"
echo "   • Upload Image: /api/upload/image/"
echo ""
echo "📊 Default Data Created:"
echo "   • 4 Menu Categories (Appetizers, Main Course, Desserts, Beverages)"
echo "   • 8 Menu Items (sample dishes)"
echo "   • 3 Sample Articles"
echo ""
echo "🛠️ Troubleshooting:"
echo "   • If API doesn't work, check cPanel Python App logs"
echo "   • Verify ALLOWED_HOSTS in settings_production.py"
echo "   • Ensure database credentials are correct"
echo ""
