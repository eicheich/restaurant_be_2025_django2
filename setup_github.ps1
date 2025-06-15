# GitHub Repository Setup Script for Windows PowerShell
# Django Restaurant API - Setup GitHub Repository

Write-Host "🔧 Setting up GitHub repository for Django Restaurant API..." -ForegroundColor Green

# Check if git is available
try {
    git --version | Out-Null
    Write-Host "✅ Git is available" -ForegroundColor Green
} catch {
    Write-Host "❌ Git is not installed! Please install Git first: https://git-scm.com/" -ForegroundColor Red
    exit 1
}

# Check if git is initialized
if (-not (Test-Path ".git")) {
    Write-Host "📝 Initializing Git repository..." -ForegroundColor Yellow
    git init
} else {
    Write-Host "✅ Git repository already exists" -ForegroundColor Green
}

# Check if .gitignore exists
if (-not (Test-Path ".gitignore")) {
    Write-Host "❌ .gitignore file not found! Please create it first." -ForegroundColor Red
    exit 1
} else {
    Write-Host "✅ .gitignore file exists" -ForegroundColor Green
}

# Add all files to git
Write-Host "📁 Adding files to git..." -ForegroundColor Yellow
git add .

# Check if there are any commits
try {
    git rev-parse --verify HEAD 2>$null | Out-Null
    Write-Host "✅ Git repository already has commits" -ForegroundColor Green
} catch {
    Write-Host "💾 Creating initial commit..." -ForegroundColor Yellow
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
}

# Display current status
Write-Host ""
Write-Host "📊 Git Status:" -ForegroundColor Cyan
git status --short

Write-Host ""
Write-Host "🚀 Next Steps:" -ForegroundColor Green
Write-Host "1. Create repository on GitHub: https://github.com/new" -ForegroundColor White
Write-Host "2. Add remote origin:" -ForegroundColor White
Write-Host "   git remote add origin https://github.com/yourusername/restaurant-api-django.git" -ForegroundColor Gray
Write-Host "3. Push to GitHub:" -ForegroundColor White
Write-Host "   git branch -M main" -ForegroundColor Gray
Write-Host "   git push -u origin main" -ForegroundColor Gray
Write-Host "4. Follow DEPLOYMENT_GUIDE_GITHUB.md for cPanel deployment" -ForegroundColor White

Write-Host ""
Write-Host "📁 Project Structure Ready:" -ForegroundColor Cyan
Write-Host "├── .gitignore                    ✅ Git ignore rules" -ForegroundColor White
Write-Host "├── README.md                     ✅ Project documentation" -ForegroundColor White
Write-Host "├── requirements.txt              ✅ Python dependencies" -ForegroundColor White
Write-Host "├── manage.py                     ✅ Django CLI" -ForegroundColor White
Write-Host "├── passenger_wsgi.py             ✅ cPanel WSGI config" -ForegroundColor White
Write-Host "├── deploy.sh                     ✅ Deployment script" -ForegroundColor White
Write-Host "├── DEPLOYMENT_GUIDE_GITHUB.md    ✅ GitHub deployment guide" -ForegroundColor White
Write-Host "├── api/                          ✅ Django API app" -ForegroundColor White
Write-Host "├── restaurant_be_2025_django/    ✅ Django settings" -ForegroundColor White
Write-Host "└── media/                        ✅ Media files" -ForegroundColor White

Write-Host ""
Write-Host "🎉 Your Django Restaurant API is ready for GitHub! 🚀" -ForegroundColor Green

# Ask if user wants to open GitHub in browser
$response = Read-Host "Would you like to open GitHub to create a new repository? (y/n)"
if ($response -eq "y" -or $response -eq "Y") {
    Start-Process "https://github.com/new"
    Write-Host "✅ GitHub opened in browser" -ForegroundColor Green
}
