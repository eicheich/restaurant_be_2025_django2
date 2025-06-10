# 🚀 Django Restaurant API - cPanel Deployment Guide

## 📋 Pre-requisites di cPanel

### 1. Setup Database MySQL
```bash
# Di cPanel MySQL Databases:
Database Name: restaurant_db
Database User: restaurant_user
Database Password: [your-secure-password]
```

### 2. Setup Python Application
```bash
# Di cPanel Python App:
Python Version: 3.8+ (recommended 3.10)
Application Root: public_html/restaurant_be_2025_django
Application URL: /restaurant-api
Startup File: passenger_wsgi.py
Entry Point: application
```

## 🔧 Configuration

### 1. Update Database Settings
Edit `restaurant_be_2025_django/settings_production.py`:

```python
# Update dengan kredensial database Anda
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cpanelusername_restaurant_db',     # Ganti dengan nama DB Anda
        'USER': 'cpanelusername_restaurant_user',   # Ganti dengan user DB Anda
        'PASSWORD': 'your_database_password',       # Ganti dengan password DB Anda
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## 🛠️ Installation

### Option 1: Automated Setup (Recommended)
```bash
# Di terminal cPanel, masuk ke folder project:
cd public_html/restaurant_be_2025_django

# Jalankan script setup lengkap:
bash complete_setup.sh
```

### Option 2: Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Check configuration
python manage.py check --settings=restaurant_be_2025_django.settings_production

# Run migrations
python manage.py migrate --settings=restaurant_be_2025_django.settings_production

# Collect static files
python manage.py collectstatic --noinput --settings=restaurant_be_2025_django.settings_production

# Create superuser
python manage.py createsuperuser --settings=restaurant_be_2025_django.settings_production

# Seed database
python manage.py seed_db --settings=restaurant_be_2025_django.settings_production
```

## 🔄 Final Steps

1. **Restart Python App** di cPanel Python App interface
2. **Test API** di: `https://yourdomain.com/restaurant-api/api/`
3. **Access Admin** di: `https://yourdomain.com/restaurant-api/admin/`

## 📡 API Endpoints

### 🍽️ Menu Management
- `GET /restaurant-api/api/menu/categories/` - List menu categories
- `POST /restaurant-api/api/menu/categories/` - Create category
- `GET /restaurant-api/api/menu/items/` - List menu items
- `POST /restaurant-api/api/menu/items/` - Create menu item

### 📰 Article Management
- `GET /restaurant-api/api/articles/` - List articles
- `POST /restaurant-api/api/articles/` - Create article

### 📸 File Upload
- `POST /restaurant-api/api/upload/image/` - Upload image

### 🔑 Admin Panel
- `https://yourdomain.com/restaurant-api/admin/` - Django Admin Interface

## 🌱 Sample Data

Setelah setup, database akan berisi:
- **4 Menu Categories**: Appetizers, Main Course, Desserts, Beverages
- **8 Menu Items**: Sample dishes dengan harga
- **3 Articles**: Sample blog posts

## 🐛 Troubleshooting

### API tidak bisa diakses
1. Cek log error di cPanel Python App
2. Pastikan `passenger_wsgi.py` benar
3. Restart Python App
4. Verify `ALLOWED_HOSTS` di settings_production.py

### Database connection error
1. Cek kredensial database di `settings_production.py`
2. Pastikan database dan user sudah dibuat di cPanel
3. Verify user privileges untuk database

### Static files tidak load
1. Jalankan `python manage.py collectstatic`
2. Cek path `STATIC_ROOT` di settings_production.py
3. Pastikan folder staticfiles ada dan writable

### Python App error
1. Cek Python version compatibility
2. Verify virtual environment path
3. Check file permissions

## 📞 Support

Jika mengalami masalah:
1. Cek file log di cPanel
2. Verify semua langkah setup
3. Pastikan file permissions benar
4. Test di development environment dulu

## 🎯 Success Indicators

✅ Python App status: Running
✅ API accessible: `https://yourdomain.com/restaurant-api/api/`
✅ Admin accessible: `https://yourdomain.com/restaurant-api/admin/`
✅ Sample data loaded successfully
✅ Image upload working

---

**🚀 Happy Coding!** Anda sekarang memiliki Django Restaurant API yang siap production di cPanel!
