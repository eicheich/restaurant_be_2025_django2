# 📋 cPanel Setup Checklist untuk Django Restaurant API

## ✅ Persiapan di cPanel

### 1. Buat Database MySQL
- [ ] Login ke cPanel
- [ ] Buka "MySQL Databases"
- [ ] Buat database baru: `restaurant_db`
- [ ] Buat user database: `restaurant_user`
- [ ] Set password untuk user
- [ ] Tambahkan user ke database dengan All Privileges

### 2. Setup Python Application
- [ ] Buka "Python App" di cPanel
- [ ] Klik "Create Application"
- [ ] Pilih Python version 3.8+
- [ ] Set Application Root: `public_html/restaurant_be_2025_django`
- [ ] Set Application URL: `/restaurant-api`
- [ ] Set Startup File: `passenger_wsgi.py`
- [ ] Set Entry Point: `application`

### 3. Upload Project Files
- [ ] Upload semua files project ke folder Application Root
- [ ] Pastikan struktur folder sesuai

### 4. Konfigurasi Database
- [ ] Edit `restaurant_be_2025_django/settings_production.py`
- [ ] Update DATABASES dengan kredensial database Anda:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'cpanelusername_restaurant_db',     # Nama database Anda
          'USER': 'cpanelusername_restaurant_user',   # User database Anda
          'PASSWORD': 'your_database_password',       # Password database Anda
          'HOST': 'localhost',
          'PORT': '3306',
      }
  }
  ```
- [ ] Update ALLOWED_HOSTS dengan domain Anda:
  ```python
  ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
  ```

### 5. Install Dependencies
- [ ] Buka Terminal di cPanel
- [ ] Masuk ke folder project: `cd public_html/restaurant_be_2025_django`
- [ ] Jalankan: `bash install_dependencies.sh`
- [ ] Atau install manual: `pip install -r requirements.txt`

### 6. Setup Database
- [ ] Jalankan: `bash setup_database.sh`
- [ ] Atau jalankan manual:
  - [ ] `python manage.py migrate --settings=restaurant_be_2025_django.settings_production`
  - [ ] `python manage.py collectstatic --noinput --settings=restaurant_be_2025_django.settings_production`
  - [ ] `python manage.py createsuperuser --settings=restaurant_be_2025_django.settings_production`
  - [ ] `python manage.py seed_db --settings=restaurant_be_2025_django.settings_production`

### 7. Restart & Test
- [ ] Restart Python App di cPanel
- [ ] Test API: `https://yourdomain.com/restaurant-api/api/`
- [ ] Test Admin: `https://yourdomain.com/restaurant-api/admin/`

## 🚀 API Endpoints yang Tersedia

### Menu Management
- `GET /restaurant-api/api/menu/categories/` - List menu categories
- `GET /restaurant-api/api/menu/items/` - List menu items
- `POST /restaurant-api/api/menu/categories/` - Create category
- `POST /restaurant-api/api/menu/items/` - Create menu item

### Article Management
- `GET /restaurant-api/api/articles/` - List articles
- `POST /restaurant-api/api/articles/` - Create article

### Upload
- `POST /restaurant-api/api/upload/image/` - Upload image

### Admin Panel
- `https://yourdomain.com/restaurant-api/admin/` - Django Admin

## 🔧 Troubleshooting

### Jika API tidak bisa diakses:
1. Cek log error di cPanel Python App
2. Pastikan passenger_wsgi.py benar
3. Restart Python App
4. Cek ALLOWED_HOSTS di settings_production.py

### Jika database error:
1. Cek koneksi database di settings_production.py
2. Pastikan database dan user sudah dibuat
3. Cek privilege user database

### Jika static files tidak load:
1. Jalankan `python manage.py collectstatic`
2. Cek path STATIC_ROOT di settings_production.py
