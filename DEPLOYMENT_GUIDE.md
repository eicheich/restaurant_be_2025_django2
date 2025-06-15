# Django Restaurant API - cPanel Deployment Guide

## 📋 Pre-Deployment Checklist

Sebelum deploy ke cPanel, pastikan project sudah siap:

- ✅ Model database (MenuCategory, MenuItem, Article)
- ✅ API endpoints dengan CRUD operations
- ✅ Image upload functionality
- ✅ Database seeder dengan 27 menu items
- ✅ Production settings (settings_production.py)
- ✅ WSGI configuration (passenger_wsgi.py)
- ✅ Requirements.txt dengan dependencies minimal

## 🚀 Deployment Steps

### Step 1: Prepare Files for Upload

1. **Zip semua files project** (kecuali folder virtual environment dan __pycache__)
   ```
   restaurant_be_2025_django/
   ├── api/
   ├── restaurant_be_2025_django/
   ├── media/
   ├── manage.py
   ├── passenger_wsgi.py
   ├── requirements.txt
   └── db.sqlite3 (optional - untuk testing data)
   ```

### Step 2: cPanel Database Setup

1. **Login ke cPanel** → MySQL Database Wizard
2. **Create Database**: `restaurant_db`
3. **Create User**: `restaurant_user`
4. **Set Password**: (simpan password yang kuat)
5. **Grant Privileges**: ALL PRIVILEGES to user on database

**📝 Catat informasi database:**
- Database Name: `cpanelusername_restaurant_db`
- Username: `cpanelusername_restaurant_user`
- Password: `[your_password]`
- Host: `localhost`

### Step 3: Update Production Settings

Edit file `restaurant_be_2025_django/settings_production.py`:

```python
# Update ALLOWED_HOSTS dengan domain Anda
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Update database credentials
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cpanelusername_restaurant_db',
        'USER': 'cpanelusername_restaurant_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

### Step 4: Upload ke cPanel

1. **File Manager** → public_html
2. **Upload** zip file dan extract
3. **Atau** upload via FTP client

### Step 5: Python Environment Setup

1. **cPanel** → Python App
2. **Create Python App**:
   - Python Version: 3.9+ (pilih yang tersedia)
   - App Directory: `restaurant_be_2025_django`
   - App URL: `/api` (atau sesuai keinginan)
   - Startup File: `passenger_wsgi.py`

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Step 6: Database Migration

Via cPanel Terminal atau SSH:

```bash
cd ~/restaurant_be_2025_django
python manage.py makemigrations --settings=restaurant_be_2025_django.settings_production
python manage.py migrate --settings=restaurant_be_2025_django.settings_production
```

### Step 7: Collect Static Files

```bash
python manage.py collectstatic --noinput --settings=restaurant_be_2025_django.settings_production
```

### Step 8: Load Sample Data (Optional)

```bash
python manage.py seed_db --settings=restaurant_be_2025_django.settings_production
```

### Step 9: Create Admin User

```bash
python manage.py createsuperuser --settings=restaurant_be_2025_django.settings_production
```

## 🧪 Testing API Endpoints

Setelah deployment, test endpoint berikut:

### Menu Categories
- `GET /api/categories/` - List all categories
- `POST /api/categories/` - Create category
- `GET /api/categories/{id}/` - Get category detail
- `PUT /api/categories/{id}/` - Update category
- `DELETE /api/categories/{id}/` - Delete category

### Menu Items
- `GET /api/menu-items/` - List all menu items
- `POST /api/menu-items/` - Create menu item
- `GET /api/menu-items/{id}/` - Get menu item detail
- `PUT /api/menu-items/{id}/` - Update menu item
- `DELETE /api/menu-items/{id}/` - Delete menu item

### Articles
- `GET /api/articles/` - List all articles
- `POST /api/articles/` - Create article
- `GET /api/articles/{id}/` - Get article detail
- `PUT /api/articles/{id}/` - Update article
- `DELETE /api/articles/{id}/` - Delete article

### Image Upload
- `POST /api/upload/` - Upload image file

## 🔧 Common Issues & Solutions

### 1. Module Not Found Error
**Problem**: `ModuleNotFoundError: No module named 'xxx'`
**Solution**: Install missing package via cPanel Python App terminal
```bash
pip install package_name
```

### 2. Database Connection Error
**Problem**: `django.db.utils.OperationalError`
**Solution**: Verify database credentials in settings_production.py

### 3. Static Files Not Loading
**Problem**: CSS/JS files not found
**Solution**: Run collectstatic and check STATIC_ROOT path

### 4. CORS Errors
**Problem**: Frontend can't access API
**Solution**: Update CORS_ALLOWED_ORIGINS in settings_production.py

### 5. Permission Denied
**Problem**: File upload fails
**Solution**: Check media folder permissions (755)

## 📱 Frontend Integration

API Base URL: `https://yourdomain.com/api/`

### Sample Frontend Code (JavaScript):

```javascript
// Fetch menu categories
const response = await fetch('https://yourdomain.com/api/categories/');
const categories = await response.json();

// Fetch menu items
const response = await fetch('https://yourdomain.com/api/menu-items/');
const menuItems = await response.json();

// Image handling (default image when null)
const imageUrl = item.image || 'https://safetypreneur.co.id/halaman/kontak-tengah';
```

## 🔒 Security Notes

- ✅ DEBUG = False in production
- ✅ Strong database password
- ✅ ALLOWED_HOSTS configured
- ✅ CORS properly configured
- ✅ XSS protection enabled

## 📞 Support

Jika mengalami masalah deployment:
1. Check cPanel Error Logs
2. Check Django logs dalam folder logs/
3. Verify semua environment variables
4. Test database connection manually

---

**✨ Selamat! API Restaurant Django Anda siap digunakan untuk development frontend dan production!**
