#!/bin/bash

# GitHub Repository Setup Script
# Run this locally to prepare your Django Restaurant API for GitHub deployment

echo "🔧 Setting up GitHub repository for Django Restaurant API..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📝 Initializing Git repository..."
    git init
else
    echo "✅ Git repository already exists"
fi

# Check if .gitignore exists
if [ ! -f ".gitignore" ]; then
    echo "❌ .gitignore file not found! Please create it first."
    exit 1
else
    echo "✅ .gitignore file exists"
fi

# Add all files to git
echo "📁 Adding files to git..."
git add .

# Create initial commit if no commits exist
if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
    echo "💾 Creating initial commit..."
    git commit -m "Initial commit: Django Restaurant API

Features:
- Complete CRUD operations for Menu Categories, Menu Items, and Articles
- Image upload functionality with default fallback
- Database seeder with 27 real Indonesian restaurant menu items
- Production-ready cPanel configuration
- GitHub deployment workflow ready

API Endpoints:
- /api/categories/ (CRUD)
- /api/menu-items/ (CRUD)
- /api/articles/ (CRUD)
- /api/upload/ (POST)
- /admin/ (Django admin)

Ready for deployment to cPanel via GitHub!"
else
    echo "✅ Git repository already has commits"
fi

# Display current status
echo ""
echo "📊 Git Status:"
git status --short

echo ""
echo "🚀 Next Steps:"
echo "1. Create repository on GitHub: https://github.com/new"
echo "2. Add remote origin:"
echo "   git remote add origin https://github.com/yourusername/restaurant-api-django.git"
echo "3. Push to GitHub:"
echo "   git branch -M main"
echo "   git push -u origin main"
echo "4. Follow DEPLOYMENT_GUIDE_GITHUB.md for cPanel deployment"

echo ""
echo "📁 Project Structure Ready:"
echo "├── .gitignore                    ✅ Git ignore rules"
echo "├── README.md                     ✅ Project documentation"
echo "├── requirements.txt              ✅ Python dependencies"
echo "├── manage.py                     ✅ Django CLI"
echo "├── passenger_wsgi.py             ✅ cPanel WSGI config"
echo "├── deploy.sh                     ✅ Deployment script"
echo "├── DEPLOYMENT_GUIDE_GITHUB.md    ✅ GitHub deployment guide"
echo "├── api/                          ✅ Django API app"
echo "├── restaurant_be_2025_django/    ✅ Django settings"
echo "└── media/                        ✅ Media files"

echo ""
echo "🎉 Your Django Restaurant API is ready for GitHub! 🚀"
