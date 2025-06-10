"""
Production settings for cPanel deployment
"""
from .settings import *
import os

# Override settings for production
DEBUG = False

# Update allowed hosts dengan domain cPanel Anda
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', '*.yourdomain.com']

# Database configuration untuk cPanel MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cpanelusername_restaurant_db',  # Ganti dengan nama database Anda
        'USER': 'cpanelusername_restaurant_user',  # Ganti dengan user database Anda
        'PASSWORD': 'your_database_password',  # Ganti dengan password database Anda
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'public_html/static')

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'public_html/media')

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# CORS settings untuk production
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "https://yourdomain.com",
    "https://www.yourdomain.com",
]
