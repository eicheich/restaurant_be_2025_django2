# Quick setup script for frontend developers (Windows PowerShell)
# Run this to get Django Restaurant API running on localhost

Write-Host "🚀 Setting up Django Restaurant API for Frontend..." -ForegroundColor Green
Write-Host ""

Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt

Write-Host ""
Write-Host "🗄️ Setting up database..." -ForegroundColor Yellow
python manage.py migrate

Write-Host ""
Write-Host "🌱 Loading sample restaurant data..." -ForegroundColor Yellow
python manage.py seed_db

Write-Host ""
Write-Host "👨‍💼 Creating admin user (optional)..." -ForegroundColor Yellow
Write-Host "You can skip this by pressing Ctrl+C" -ForegroundColor Gray
python manage.py createsuperuser

Write-Host ""
Write-Host "🎉 Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "📡 API Endpoints ready at:" -ForegroundColor Cyan
Write-Host "   - Categories: http://localhost:8000/api/menu/categories/" -ForegroundColor White
Write-Host "   - Menu Items: http://localhost:8000/api/menu/items/" -ForegroundColor White
Write-Host "   - Articles:   http://localhost:8000/api/articles/" -ForegroundColor White
Write-Host "   - Admin:      http://localhost:8000/admin/" -ForegroundColor White
Write-Host ""
Write-Host "🏃‍♂️ Starting development server..." -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host ""
python manage.py runserver
