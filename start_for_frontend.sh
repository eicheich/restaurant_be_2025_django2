#!/bin/bash
# Quick setup script for frontend developers
# Run this to get Django Restaurant API running on localhost

echo "🚀 Setting up Django Restaurant API for Frontend..."
echo ""

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "🗄️ Setting up database..."
python manage.py migrate

echo ""
echo "🌱 Loading sample restaurant data..."
python manage.py seed_db

echo ""
echo "👨‍💼 Creating admin user (optional)..."
echo "You can skip this by pressing Ctrl+C"
python manage.py createsuperuser

echo ""
echo "🎉 Setup complete!"
echo ""
echo "📡 API Endpoints ready at:"
echo "   - Categories: http://localhost:8000/api/menu/categories/"
echo "   - Menu Items: http://localhost:8000/api/menu/items/"
echo "   - Articles:   http://localhost:8000/api/articles/"
echo "   - Admin:      http://localhost:8000/admin/"
echo ""
echo "🏃‍♂️ Starting development server..."
echo "Press Ctrl+C to stop the server"
echo ""
python manage.py runserver
