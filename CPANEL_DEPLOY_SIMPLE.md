# Simple cPanel Deployment Guide

## Step 1: Upload Files
1. Zip your project folder
2. Upload to cPanel File Manager
3. Extract in your domain folder (e.g., `public_html/api` or `public_html`)

## Step 2: Create Python App in cPanel
1. Go to "Python App" in cPanel
2. Click "Create Application"
3. Choose Python version 3.10+
4. Set Application Root: `/home/yourusername/public_html/api` (adjust path)
5. Set Application URL: `api` (or whatever you want)
6. Click "Create"

## Step 3: Install Requirements
1. In Python App, click "Open Terminal"
2. Run: `pip install -r requirements.txt`

## Step 4: Database Setup
1. Create MySQL database in cPanel
2. Create MySQL user and assign to database
3. Note down: database name, username, password, host

## Step 5: Configure Settings
Edit `restaurant_be_2025_django/settings_production.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',  # or your host
        'PORT': '3306',
    }
}
```

## Step 6: Run Django Commands
In terminal:
```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
python manage.py seed_db  # Optional: add sample data
```

## Step 7: Restart App
In Python App interface, click "Restart"

## Step 8: Test
Visit: `yourdomain.com/api/menu-categories/`

That's it! Keep it simple.
