# Django Restaurant API - cPanel Deployment

## Quick Setup (Keep it Simple!)

### 1. Upload to cPanel
- Zip this entire folder
- Upload to cPanel File Manager
- Extract in `public_html/api` (or wherever you want)

### 2. Create Python App
- cPanel → Python App → Create Application
- Python Version: 3.10+
- Application Root: `/home/yourusername/public_html/api`
- Application URL: `api`

### 3. Install Requirements
In Python App terminal:
```bash
pip install -r requirements.txt
```

### 4. Setup Database
- cPanel → MySQL Databases
- Create database: `restaurant_db`
- Create user: `restaurant_user`
- Set password and grant privileges
- Edit `restaurant_be_2025_django/settings_production.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourusername_restaurant_db',    # Add your cPanel username prefix
        'USER': 'yourusername_restaurant_user',  # Add your cPanel username prefix
        'PASSWORD': 'your_password_here',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run Setup Commands
In Python App terminal:

**Method 1: Test database first**
```bash
# Test if database connection works
python test_db_connection.py
```

**Method 2: If database connection is OK, but still "No migrations to apply":**
```bash
# Check what migrations Django sees
python manage.py showmigrations --settings=restaurant_be_2025_django.settings_production

# If no migrations shown, Django is using wrong settings
# Force create migrations with production settings
python manage.py makemigrations api --settings=restaurant_be_2025_django.settings_production

# Then migrate
python manage.py migrate --settings=restaurant_be_2025_django.settings_production
```

**Method 3: Use the automated script:**
```bash
# Make script executable and run
chmod +x cpanel_setup.sh
./cpanel_setup.sh
```

**Method 4: Manual step by step:**
```bash
# Set environment variable first
export DJANGO_SETTINGS_MODULE=restaurant_be_2025_django.settings_production

# Then run commands
python manage.py makemigrations api
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
python manage.py seed_db
```

### 6. Restart & Test
- Click "Restart" in Python App
- Visit: `yourdomain.com/api/menu-categories/`

## API Endpoints
- `/api/menu-categories/` - Menu categories CRUD
- `/api/menu-items/` - Menu items CRUD
- `/api/articles/` - Articles CRUD
- `/api/upload/` - Image upload
- `/admin/` - Django admin interface

That's it! Simple and straightforward.
