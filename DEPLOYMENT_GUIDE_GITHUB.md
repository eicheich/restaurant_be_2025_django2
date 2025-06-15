# Django Restaurant API - GitHub + cPanel Deployment Guide

## 🚀 Modern Deployment: GitHub → cPanel Python Application

Panduan ini menjelaskan cara deploy Django Restaurant API ke cPanel menggunakan GitHub repository dan Python Application feature.

## 📋 Pre-Deployment Checklist

- ✅ Project Django sudah complete dan tested locally
- ✅ GitHub repository sudah dibuat
- ✅ cPanel hosting dengan Python Application support
- ✅ MySQL database access di cPanel

## 🔄 Deployment Workflow Overview

```
Local Development → GitHub Repository → cPanel Python App → Production
```

---

## 📚 Step 1: Prepare GitHub Repository

### 1.1 Create .gitignore
Mari buat file `.gitignore` untuk Django project:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Media files (optional - uncomment if you don't want to track media)
# media/

# Static files
staticfiles/
static_collected/

# Environment variables
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Deployment
*.zip
*.tar.gz
```

### 1.2 Initialize Git Repository
```powershell
# Navigate to project directory
cd "c:\1 kill\Python\django\restaurant_be_2025_django"

# Initialize git repository
git init

# Add gitignore
# (create .gitignore file with content above)

# Add all files
git add .

# Initial commit
git commit -m "Initial commit: Django Restaurant API with CRUD operations"

# Add remote repository (replace with your GitHub repo URL)
git remote add origin https://github.com/yourusername/restaurant-api-django.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 1.3 Repository Structure for cPanel
Pastikan repository structure seperti ini:
```
restaurant-api-django/                 # GitHub repo root
├── .gitignore                        # Git ignore file
├── README.md                         # Project documentation
├── requirements.txt                  # Python dependencies
├── manage.py                        # Django CLI
├── passenger_wsgi.py                # cPanel WSGI config
├── DEPLOYMENT_GUIDE_GITHUB.md       # This guide
├── api/                             # Django app
├── restaurant_be_2025_django/        # Django settings
└── media/                           # Media files
```

---

## 🗄️ Step 2: cPanel Database Setup

### 2.1 Create MySQL Database
1. **Login ke cPanel** → **MySQL Database Wizard**
2. **Create Database**: `restaurant_api_db`
3. **Create Database User**: `restaurant_api_user`
4. **Set Strong Password**: (save this password securely)
5. **Grant Privileges**: Select **ALL PRIVILEGES**

### 2.2 Note Database Information
```
Database Name: cpanelusername_restaurant_api_db
Username: cpanelusername_restaurant_api_user
Password: [your_secure_password]
Host: localhost
Port: 3306
```

---

## 🐍 Step 3: cPanel Python Application Setup

### 3.1 Create Python Application
1. **Login ke cPanel** → **Python App**
2. **Create Application**:
   - **Python Version**: 3.9 atau 3.10 (pilih yang tersedia)
   - **Application Root**: `restaurant_api` (atau nama yang Anda inginkan)
   - **Application URL**: `/api` (akan menjadi yourdomain.com/api)
   - **Application Startup File**: `passenger_wsgi.py`
   - **Application Entry Point**: `application`

3. **Python Application akan create**:
   - Virtual environment otomatis
   - Application directory di `~/restaurant_api/`
   - Public access via domain/api

### 3.2 Note Application Information
cPanel akan provide:
```
Application Root: /home/cpanelusername/restaurant_api/
Virtual Environment: /home/cpanelusername/virtualenv/restaurant_api/3.x/
Application URL: https://yourdomain.com/api/
```

---

## 📥 Step 4: Deploy from GitHub

### 4.1 Clone Repository
Via cPanel Terminal atau SSH:

```bash
# Navigate to application directory
cd ~/restaurant_api

# Clone your GitHub repository
git clone https://github.com/yourusername/restaurant-api-django.git .

# Verify files
ls -la
```

### 4.2 Alternative: Upload ZIP
Jika prefer upload manual:
1. Download ZIP dari GitHub repository
2. Upload ke cPanel File Manager
3. Extract ke application directory (`~/restaurant_api/`)

---

## ⚙️ Step 5: Configure Production Settings

### 5.1 Update settings_production.py
Edit file `restaurant_be_2025_django/settings_production.py`:

```python
"""
Production settings for cPanel deployment via GitHub
"""
from .settings import *
import os

# Production settings
DEBUG = False

# IMPORTANT: Update with your actual domain
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', 'your-subdomain.cpanel-host.com']

# Database configuration for cPanel MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cpanelusername_restaurant_api_db',      # Your database name
        'USER': 'cpanelusername_restaurant_api_user',    # Your database user
        'PASSWORD': 'your_secure_password',              # Your database password
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Static files configuration for cPanel
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'public_html/static/')

# Media files configuration for cPanel
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'public_html/media/')

# CORS configuration for production
CORS_ALLOWED_ORIGINS = [
    "https://yourdomain.com",
    "https://www.yourdomain.com",
    # Add your frontend domains here
]

# Security settings for production
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True  # Enable if you have SSL
SECURE_HSTS_SECONDS = 31536000  # Enable if you have SSL
```

### 5.2 Verify passenger_wsgi.py
Ensure your `passenger_wsgi.py` is correct:

```python
import os
import sys

# Add project to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Set Django settings for production
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_be_2025_django.settings_production')

# Setup Django
import django
django.setup()

# Import WSGI application
from restaurant_be_2025_django.wsgi import application
```

---

## 📦 Step 6: Install Dependencies

### 6.1 Activate Virtual Environment & Install
Via cPanel Terminal:

```bash
# Navigate to app directory
cd ~/restaurant_api

# Activate virtual environment (cPanel will show the exact path)
source /home/cpanelusername/virtualenv/restaurant_api/3.x/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt

# Verify installations
pip list
```

### 6.2 Install Additional cPanel-specific Packages
```bash
# Install additional packages if needed
pip install mysqlclient  # Alternative to PyMySQL
pip install gunicorn     # If needed for some cPanel configurations
```

---

## 🗄️ Step 7: Database Migration & Setup

### 7.1 Run Migrations
```bash
# Make sure you're in the app directory and virtual environment is active
cd ~/restaurant_api

# Run migrations
python manage.py makemigrations --settings=restaurant_be_2025_django.settings_production
python manage.py migrate --settings=restaurant_be_2025_django.settings_production

# Verify migration
python manage.py showmigrations --settings=restaurant_be_2025_django.settings_production
```

### 7.2 Collect Static Files
```bash
# Collect static files for production
python manage.py collectstatic --noinput --settings=restaurant_be_2025_django.settings_production
```

### 7.3 Load Sample Data
```bash
# Load initial data (27 menu items + categories)
python manage.py seed_db --settings=restaurant_be_2025_django.settings_production
```

### 7.4 Create Admin User
```bash
# Create superuser for admin access
python manage.py createsuperuser --settings=restaurant_be_2025_django.settings_production
```

---

## 🔄 Step 8: Restart Python Application

### 8.1 Restart via cPanel
1. **cPanel** → **Python App**
2. Find your application
3. Click **Restart** button
4. Wait for restart to complete

### 8.2 Alternative: Touch Restart File
```bash
# Create/touch restart file
touch ~/restaurant_api/tmp/restart.txt
```

---

## 🧪 Step 9: Test Deployment

### 9.1 Test API Endpoints
Visit these URLs in browser or API client:

**Base URL**: `https://yourdomain.com/api/`

- ✅ `GET https://yourdomain.com/api/categories/` - List categories
- ✅ `GET https://yourdomain.com/api/menu-items/` - List menu items
- ✅ `GET https://yourdomain.com/api/articles/` - List articles
- ✅ `POST https://yourdomain.com/api/upload/` - Test upload

### 9.2 Test Admin Panel
- ✅ `https://yourdomain.com/admin/` - Django admin interface

### 9.3 Test CORS (if using frontend)
```javascript
// Test from browser console on your frontend domain
fetch('https://yourdomain.com/api/categories/')
  .then(response => response.json())
  .then(data => console.log(data));
```

---

## 🔄 Step 10: Continuous Deployment Workflow

### 10.1 Update Deployment Process
For future updates, follow this workflow:

```bash
# 1. Local development
# Make changes to your code locally

# 2. Commit to GitHub
git add .
git commit -m "Update: description of changes"
git push origin main

# 3. Pull updates on cPanel
cd ~/restaurant_api
git pull origin main

# 4. Update dependencies (if changed)
pip install -r requirements.txt

# 5. Run migrations (if models changed)
python manage.py migrate --settings=restaurant_be_2025_django.settings_production

# 6. Collect static files (if static files changed)
python manage.py collectstatic --noinput --settings=restaurant_be_2025_django.settings_production

# 7. Restart application
touch tmp/restart.txt
```

### 10.2 Automated Deployment Script
Create `deploy.sh` for easier updates:

```bash
#!/bin/bash
echo "🚀 Deploying Django Restaurant API..."

# Pull latest changes
git pull origin main

# Install/update dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate --settings=restaurant_be_2025_django.settings_production

# Collect static files
python manage.py collectstatic --noinput --settings=restaurant_be_2025_django.settings_production

# Restart application
touch tmp/restart.txt

echo "✅ Deployment completed!"
echo "🌐 API available at: https://yourdomain.com/api/"
```

Make it executable:
```bash
chmod +x deploy.sh
```

---

## 🔧 Troubleshooting

### Common Issues & Solutions

#### 1. Import Error / Module Not Found
```bash
# Ensure virtual environment is activated
source /home/cpanelusername/virtualenv/restaurant_api/3.x/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

#### 2. Database Connection Error
- Verify database credentials in `settings_production.py`
- Check if database and user exist in cPanel MySQL
- Test database connection manually

#### 3. Static Files Not Loading
```bash
# Recollect static files
python manage.py collectstatic --clear --noinput --settings=restaurant_be_2025_django.settings_production
```

#### 4. Application Not Starting
- Check cPanel Error Logs
- Verify `passenger_wsgi.py` configuration
- Ensure Python version compatibility

#### 5. CORS Errors
- Update `CORS_ALLOWED_ORIGINS` in `settings_production.py`
- Add your frontend domain to allowed origins

### Debug Commands
```bash
# Check Python path and Django settings
python -c "import sys; print(sys.path)"
python -c "import django; print(django.get_version())"

# Test Django setup
python manage.py check --settings=restaurant_be_2025_django.settings_production

# Test database connection
python manage.py shell --settings=restaurant_be_2025_django.settings_production
>>> from django.db import connection
>>> connection.ensure_connection()
```

---

## 📱 Frontend Integration

### Production API Base URL
```javascript
const API_BASE_URL = 'https://yourdomain.com/api';

// Fetch data
const fetchMenuItems = async () => {
  const response = await fetch(`${API_BASE_URL}/menu-items/`);
  return response.json();
};
```

---

## 🔒 Security Checklist

- ✅ `DEBUG = False` in production
- ✅ Strong database password
- ✅ `ALLOWED_HOSTS` properly configured
- ✅ `CORS_ALLOWED_ORIGINS` restricted to your domains
- ✅ SSL/HTTPS enabled (recommended)
- ✅ Regular security updates

---

## 🎉 Deployment Complete!

Your Django Restaurant API is now successfully deployed using GitHub + cPanel Python Application!

### 🌐 Access Points:
- **API Endpoints**: `https://yourdomain.com/api/`
- **Admin Panel**: `https://yourdomain.com/admin/`
- **GitHub Repository**: `https://github.com/yourusername/restaurant-api-django`

### 🔄 Next Updates:
1. Make changes locally
2. Push to GitHub
3. Pull on cPanel
4. Run deployment script
5. Restart application

**Your restaurant API is now live and ready for frontend integration! 🚀**
