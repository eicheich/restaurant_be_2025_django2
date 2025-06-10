# Restaurant Backend API (Django Version)

A Django REST Framework API for a restaurant application with menu and article management capabilities.

## Features

1. **Menu Management**
   - CRUD operations for menu categories
   - CRUD operations for menu items
   - Filter items by category

2. **Article/Blog Management**
   - CRUD operations for articles
   - Automatic slug generation from article titles
   - Publication status control (published/draft)

3. **Image Upload**
   - Upload images for menu items and articles
   - Secure file storage with unique file names

4. **API Documentation**
   - Built-in DRF browsable API
   - Swagger/OpenAPI documentation (optional)

## Tech Stack

- Django 4.2.x
- Django REST Framework
- MySQL
- Pillow (Image processing)
- django-cors-headers (CORS support)
- Python-slugify (Slug generation)

## Project Structure

```
restaurant_be_2025_django/
├── api/                        # Main Django app
│   ├── management/            # Custom Django management commands
│   │   └── commands/          # Management commands like seed_db
│   ├── migrations/            # Database migrations
│   ├── models.py              # Database models
│   ├── serializers/           # DRF serializers
│   ├── utils/                 # Utility functions
│   └── views/                 # API views and viewsets
├── media/                     # User uploaded files
│   └── images/                # Uploaded images
├── restaurant_be_2025_django/ # Project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   └── wsgi.py                # WSGI configuration
├── static/                    # Static files
├── manage.py                  # Django command-line utility
├── passenger_wsgi.py          # cPanel configuration
├── Procfile                   # Heroku/PythonAnywhere configuration
└── requirements.txt           # Project dependencies
```

## API Endpoints

### Menu Endpoints

- `GET /api/menu/categories/` - List all menu categories
- `GET /api/menu/categories/{id}/` - Retrieve a specific menu category
- `POST /api/menu/categories/` - Create a new menu category
- `PUT/PATCH /api/menu/categories/{id}/` - Update a menu category
- `DELETE /api/menu/categories/{id}/` - Delete a menu category

- `GET /api/menu/items/` - List all menu items
- `GET /api/menu/items/{id}/` - Retrieve a specific menu item
- `POST /api/menu/items/` - Create a new menu item
- `PUT/PATCH /api/menu/items/{id}/` - Update a menu item
- `DELETE /api/menu/items/{id}/` - Delete a menu item
- `GET /api/menu/items/category/{category_id}/` - List items by category

### Article Endpoints

- `GET /api/articles/` - List all articles
- `GET /api/articles/{slug|id}/` - Retrieve a specific article (by slug or ID)
- `POST /api/articles/` - Create a new article
- `PUT/PATCH /api/articles/{slug|id}/` - Update an article
- `DELETE /api/articles/{slug|id}/` - Delete an article

### Upload Endpoint

- `POST /api/upload/image/` - Upload an image

## Installation and Setup

### Prerequisites

- Python 3.10 or higher
- MySQL 5.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/restaurant_be_2025_django.git
cd restaurant_be_2025_django
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure the database**

Edit the `restaurant_be_2025_django/settings.py` file to configure your database connection:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. **Run migrations**

```bash
python manage.py migrate
```

6. **Create a superuser**

```bash
python manage.py createsuperuser
```

7. **Seed the database with sample data (optional)**

```bash
python manage.py seed_db
```

8. **Start the development server**

```bash
python manage.py runserver
```

The API will be available at http://127.0.0.1:8000/api/

## Deployment

### cPanel Deployment

Setelah git clone di cPanel, ikuti langkah berikut:

#### 1. Setup Python App di cPanel
1. Login ke cPanel
2. Cari "Python App" atau "Setup Python App"
3. Klik "Create Application"
4. Pilih Python version 3.8+
5. Set Application Root ke folder project
6. Set Application URL (contoh: `/restaurant-api`)

#### 2. Konfigurasi Database
1. Buat database MySQL di cPanel
2. Catat nama database, username, dan password
3. Copy `.env.example` menjadi `.env`
4. Update file `.env` dengan kredensial database Anda

#### 3. Update Settings Production
Edit file `restaurant_be_2025_django/settings_production.py`:
```python
# Update dengan informasi Anda
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

#### 4. Install Dependencies dan Setup
Jalankan di terminal cPanel:
```bash
# Masuk ke folder project
cd public_html/restaurant_be_2025_django

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate --settings=restaurant_be_2025_django.settings_production

# Collect static files
python manage.py collectstatic --noinput --settings=restaurant_be_2025_django.settings_production

# Create superuser
python manage.py createsuperuser --settings=restaurant_be_2025_django.settings_production

# Seed database
python manage.py seed_db --settings=restaurant_be_2025_django.settings_production
```

#### 5. Update passenger_wsgi.py
Pastikan file `passenger_wsgi.py` menggunakan path Python environment yang benar di cPanel Anda.

#### 6. Restart Python App
Di cPanel Python App interface, klik "Restart" untuk menerapkan perubahan.

#### 7. Test API
API akan tersedia di: `https://yourdomain.com/restaurant-api/api/`

### Heroku Deployment

1. Create a Heroku account and install the Heroku CLI
2. Log in to Heroku: `heroku login`
3. Create a new Heroku app: `heroku create your-app-name`
4. Add a database: `heroku addons:create heroku-postgresql:hobby-dev`
5. Deploy the application: `git push heroku main`
6. Run migrations: `heroku run python manage.py migrate`

## License

This project is licensed under the MIT License - see the LICENSE file for details.
