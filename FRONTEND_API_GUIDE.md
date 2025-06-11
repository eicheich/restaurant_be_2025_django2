# Django Restaurant API - Frontend Integration Guide

## 🚀 Quick Start untuk Frontend Developer

### 1. Setup Backend Django (Localhost)

**Clone & Setup:**
```bash
git clone [repository-url]
cd restaurant_be_2025_django
```

**Install Dependencies:**
```bash
pip install -r requirements.txt
```

**Setup Database & Data:**
```bash
# Run migrations
python manage.py migrate

# Create admin user (optional)
python manage.py createsuperuser

# Load sample restaurant data
python manage.py seed_db
```

**Start Server:**
```bash
python manage.py runserver
```

✅ **API Ready at:** `http://localhost:8000/api/`

---

## 📡 API Endpoints untuk Frontend

### **Base URL:** `http://localhost:8000/api/`

### 🍽️ **Menu Categories**
```
GET    /api/menu/categories/     - List all categories
POST   /api/menu/categories/     - Create new category
GET    /api/menu/categories/{id}/ - Get specific category
PUT    /api/menu/categories/{id}/ - Update category
DELETE /api/menu/categories/{id}/ - Delete category
```

### 🥘 **Menu Items**
```
GET    /api/menu/items/     - List all menu items
POST   /api/menu/items/     - Create new menu item
GET    /api/menu/items/{id}/ - Get specific menu item
PUT    /api/menu/items/{id}/ - Update menu item
DELETE /api/menu/items/{id}/ - Delete menu item
```

### 📰 **Articles**
```
GET    /api/articles/     - List all articles
POST   /api/articles/     - Create new article
GET    /api/articles/{id}/ - Get specific article
PUT    /api/articles/{id}/ - Update article
DELETE /api/articles/{id}/ - Delete article
```

### 📤 **File Upload**
```
POST   /api/upload/image/  - Upload image file
```

---

## 📊 Sample Data Structure

### **Menu Categories Response:**
```json
[
  {
    "id": 1,
    "name": "Menu Paket",
    "description": "Paket menu lengkap dengan nasi dan minuman",
    "created_at": "2025-06-11T12:00:00Z",
    "updated_at": "2025-06-11T12:00:00Z"
  },
  {
    "id": 2,
    "name": "Minuman",
    "description": "Minuman segar dan hangat",
    "created_at": "2025-06-11T12:00:00Z",
    "updated_at": "2025-06-11T12:00:00Z"
  }
]
```

### **Menu Items Response:**
```json
[
  {
    "id": 1,
    "category": {
      "id": 1,
      "name": "Menu Paket",
      "description": "Paket menu lengkap dengan nasi dan minuman"
    },
    "name": "Paket Nila Bakar/Goreng + Nasi + Es Teh",
    "description": "Paket lengkap nila bakar atau goreng dengan nasi dan es teh",
    "price": "29000.00",
    "image": "http://localhost:8000/media/dummy/image-dummy.jpg",
    "is_available": true,
    "created_at": "2025-06-11T12:00:00Z",
    "updated_at": "2025-06-11T12:00:00Z"
  }
]
```

### **Articles Response:**
```json
[
  {
    "id": 1,
    "title": "Selamat Datang di Restoran Kami",
    "content": "Restoran kami menyajikan berbagai menu khas...",
    "image": "http://localhost:8000/media/dummy/image-dummy.jpg",
    "is_published": true,
    "created_at": "2025-06-11T12:00:00Z",
    "updated_at": "2025-06-11T12:00:00Z"
  }
]
```

---

## 💡 Frontend Implementation Examples

### **Fetch Menu Categories (JavaScript):**
```javascript
// Get all menu categories
const getMenuCategories = async () => {
  try {
    const response = await fetch('http://localhost:8000/api/menu/categories/');
    const categories = await response.json();
    console.log('Categories:', categories);
    return categories;
  } catch (error) {
    console.error('Error fetching categories:', error);
  }
};
```

### **Fetch Menu Items by Category:**
```javascript
// Get menu items (can filter by category)
const getMenuItems = async (categoryId = null) => {
  let url = 'http://localhost:8000/api/menu/items/';
  if (categoryId) {
    url += `?category=${categoryId}`;
  }

  try {
    const response = await fetch(url);
    const items = await response.json();
    console.log('Menu Items:', items);
    return items;
  } catch (error) {
    console.error('Error fetching menu items:', error);
  }
};
```

### **Create New Menu Item:**
```javascript
const createMenuItem = async (itemData) => {
  try {
    const response = await fetch('http://localhost:8000/api/menu/items/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(itemData)
    });

    const newItem = await response.json();
    console.log('Created item:', newItem);
    return newItem;
  } catch (error) {
    console.error('Error creating menu item:', error);
  }
};

// Example usage:
const newItem = {
  category: 1,
  name: "Nasi Gudeg",
  description: "Nasi gudeg khas Yogyakarta",
  price: "15000",
  is_available: true
};
createMenuItem(newItem);
```

### **Upload Image:**
```javascript
const uploadImage = async (file) => {
  const formData = new FormData();
  formData.append('image', file);

  try {
    const response = await fetch('http://localhost:8000/api/upload/image/', {
      method: 'POST',
      body: formData
    });

    const result = await response.json();
    console.log('Upload result:', result);
    return result.image_url; // Returns the uploaded image URL
  } catch (error) {
    console.error('Error uploading image:', error);
  }
};
```

---

## 🎯 Available Sample Data

Setelah menjalankan `python manage.py seed_db`, Anda akan memiliki:

### **4 Kategori Menu:**
1. **Menu Paket** (2 items)
2. **Minuman** (8 items)
3. **Menu Makanan** (7 items)
4. **Cemilan** (10 items)

### **27 Menu Items**, contoh:
- Paket Nila Bakar/Goreng + Nasi + Es Teh - Rp 29,000
- Jeruk Panas/Es - Rp 5,000
- 1 Kg Nila Bakar/Goreng - Rp 65,000
- Mendoan - Rp 6,000
- Dan lainnya...

### **3 Sample Articles:**
- Selamat Datang di Restoran Kami
- Menu Spesial: Nila Bakar Khas Jepara
- Promo Spesial Bulan Ini

---

## 🔧 CORS Setup (Jika Diperlukan)

Jika frontend Anda berjalan di port yang berbeda (misalnya React di port 3000), CORS sudah dikonfigurasi. Tapi jika ada masalah, bisa menambahkan:

```python
# Di settings.py sudah ada:
CORS_ALLOW_ALL_ORIGINS = True  # Untuk development
```

---

## 🐛 Troubleshooting

### **Server tidak bisa diakses:**
```bash
# Pastikan server berjalan
python manage.py runserver

# Atau dengan host dan port spesifik
python manage.py runserver 0.0.0.0:8000
```

### **Data tidak ada:**
```bash
# Jalankan ulang seeder
python manage.py seed_db
```

### **CORS Error:**
- Pastikan `django-cors-headers` terinstall
- Check `CORS_ALLOW_ALL_ORIGINS = True` di settings.py

### **Image tidak muncul:**
- Pastikan ada file `media/dummy/image-dummy.jpg`
- Check `MEDIA_URL` dan `MEDIA_ROOT` di settings.py

---

## 📱 Testing API dengan Browser/Postman

**Test URLs:**
- Categories: http://localhost:8000/api/menu/categories/
- Menu Items: http://localhost:8000/api/menu/items/
- Articles: http://localhost:8000/api/articles/
- Admin Panel: http://localhost:8000/admin/

**Happy Coding! 🚀**

---

## 📞 Need Help?

Jika ada masalah dengan API:
1. Check apakah server Django berjalan
2. Check console browser untuk error CORS/Network
3. Test endpoint dengan Postman/browser dulu
4. Pastikan data sudah di-seed dengan benar
