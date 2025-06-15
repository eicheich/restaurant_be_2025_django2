# 🎯 Django Restaurant API - Ready for Frontend Development

## ✅ Project Status: COMPLETE & READY

**Local Development URL**: `http://127.0.0.1:8000/api/`
**Production Deployment**: Ready for cPanel (see DEPLOYMENT_GUIDE.md)

## 🚀 Quick Start for Frontend Developers

### 1. Start API Server
```powershell
cd "c:\1 kill\Python\django\restaurant_be_2025_django"
python manage.py runserver 8000
```

### 2. API Base URL
```
http://localhost:8000/api/
```

### 3. Available Endpoints

#### Menu Categories
- `GET /api/categories/` - List all categories (4 categories)
- `POST /api/categories/` - Create new category
- `GET /api/categories/{id}/` - Get category detail
- `PUT /api/categories/{id}/` - Update category
- `DELETE /api/categories/{id}/` - Delete category

#### Menu Items
- `GET /api/menu-items/` - List all menu items (27 items)
- `POST /api/menu-items/` - Create new menu item
- `GET /api/menu-items/{id}/` - Get menu item detail
- `PUT /api/menu-items/{id}/` - Update menu item
- `DELETE /api/menu-items/{id}/` - Delete menu item

#### Articles
- `GET /api/articles/` - List all articles (3 articles)
- `POST /api/articles/` - Create new article
- `GET /api/articles/{id}/` - Get article detail
- `PUT /api/articles/{id}/` - Update article
- `DELETE /api/articles/{id}/` - Delete article

#### File Upload
- `POST /api/upload/` - Upload image files

## 📊 Sample Data Available

After running the API, you'll have access to:

### 4 Menu Categories:
1. **Menu Paket** - Paket makanan lengkap
2. **Minuman** - Berbagai minuman segar
3. **Menu Makanan** - Makanan utama
4. **Cemilan** - Snack dan makanan ringan

### 27 Real Menu Items with Indonesian Food:
- Nasi Gudeg Yogya (Rp 25,000)
- Ayam Bakar Taliwang (Rp 35,000)
- Sate Kambing Madura (Rp 30,000)
- Rendang Padang (Rp 40,000)
- Gado-gado Jakarta (Rp 20,000)
- Es Teh Manis (Rp 8,000)
- Jus Alpukat (Rp 15,000)
- Keripik Tempe (Rp 12,000)
- And 19 more...

### 3 Sample Articles:
- Indonesian Culinary Heritage
- Traditional Cooking Methods
- Regional Food Specialties

## 💻 Frontend Integration Examples

### React.js Example:
```jsx
import { useState, useEffect } from 'react';

function MenuApp() {
  const [categories, setCategories] = useState([]);
  const [menuItems, setMenuItems] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      setLoading(true);

      const [categoriesRes, itemsRes] = await Promise.all([
        fetch('http://localhost:8000/api/categories/'),
        fetch('http://localhost:8000/api/menu-items/')
      ]);

      const categoriesData = await categoriesRes.json();
      const itemsData = await itemsRes.json();

      setCategories(categoriesData);
      setMenuItems(itemsData);
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setLoading(false);
    }
  };

  const getImageUrl = (item) => {
    return item.image || 'https://safetypreneur.co.id/halaman/kontak-tengah';
  };

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      <h1>Restaurant Menu</h1>

      <h2>Categories ({categories.length})</h2>
      <div className="categories">
        {categories.map(category => (
          <div key={category.id} className="category-card">
            <img src={getImageUrl(category)} alt={category.name} />
            <h3>{category.name}</h3>
            <p>{category.description}</p>
          </div>
        ))}
      </div>

      <h2>Menu Items ({menuItems.length})</h2>
      <div className="menu-items">
        {menuItems.map(item => (
          <div key={item.id} className="menu-item-card">
            <img src={getImageUrl(item)} alt={item.name} />
            <h3>{item.name}</h3>
            <p>{item.description}</p>
            <p className="price">Rp {item.price}</p>
            <p className="category">Category: {item.category_name}</p>
            {item.is_available ? (
              <span className="available">Available</span>
            ) : (
              <span className="unavailable">Not Available</span>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}

export default MenuApp;
```

### Vue.js Example:
```vue
<template>
  <div id="app">
    <h1>Restaurant Menu</h1>

    <div v-if="loading">Loading...</div>

    <div v-else>
      <h2>Categories ({{ categories.length }})</h2>
      <div class="categories">
        <div v-for="category in categories" :key="category.id" class="category-card">
          <img :src="getImageUrl(category)" :alt="category.name" />
          <h3>{{ category.name }}</h3>
          <p>{{ category.description }}</p>
        </div>
      </div>

      <h2>Menu Items ({{ menuItems.length }})</h2>
      <div class="menu-items">
        <div v-for="item in menuItems" :key="item.id" class="menu-item-card">
          <img :src="getImageUrl(item)" :alt="item.name" />
          <h3>{{ item.name }}</h3>
          <p>{{ item.description }}</p>
          <p class="price">Rp {{ item.price }}</p>
          <p class="category">Category: {{ item.category_name }}</p>
          <span v-if="item.is_available" class="available">Available</span>
          <span v-else class="unavailable">Not Available</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MenuApp',
  data() {
    return {
      categories: [],
      menuItems: [],
      loading: true
    }
  },
  async mounted() {
    await this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        this.loading = true;

        const [categoriesRes, itemsRes] = await Promise.all([
          fetch('http://localhost:8000/api/categories/'),
          fetch('http://localhost:8000/api/menu-items/')
        ]);

        this.categories = await categoriesRes.json();
        this.menuItems = await itemsRes.json();
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        this.loading = false;
      }
    },
    getImageUrl(item) {
      return item.image || 'https://safetypreneur.co.id/halaman/kontak-tengah';
    }
  }
}
</script>
```

### Vanilla JavaScript Example:
```javascript
// Simple fetch example
async function loadRestaurantData() {
  try {
    // Fetch categories
    const categoriesResponse = await fetch('http://localhost:8000/api/categories/');
    const categories = await categoriesResponse.json();
    console.log('Categories:', categories);

    // Fetch menu items
    const menuItemsResponse = await fetch('http://localhost:8000/api/menu-items/');
    const menuItems = await menuItemsResponse.json();
    console.log('Menu Items:', menuItems);

    // Display categories
    const categoriesContainer = document.getElementById('categories');
    categories.forEach(category => {
      const categoryElement = document.createElement('div');
      categoryElement.innerHTML = `
        <h3>${category.name}</h3>
        <p>${category.description}</p>
        <img src="${category.image || 'https://safetypreneur.co.id/halaman/kontak-tengah'}" alt="${category.name}" style="width: 200px;">
      `;
      categoriesContainer.appendChild(categoryElement);
    });

    // Display menu items
    const menuContainer = document.getElementById('menu-items');
    menuItems.forEach(item => {
      const itemElement = document.createElement('div');
      itemElement.innerHTML = `
        <h3>${item.name}</h3>
        <p>${item.description}</p>
        <p><strong>Price: Rp ${item.price}</strong></p>
        <p>Category: ${item.category_name}</p>
        <p>Available: ${item.is_available ? 'Yes' : 'No'}</p>
        <img src="${item.image || 'https://safetypreneur.co.id/halaman/kontak-tengah'}" alt="${item.name}" style="width: 200px;">
      `;
      menuContainer.appendChild(itemElement);
    });

  } catch (error) {
    console.error('Error loading data:', error);
  }
}

// Call function when page loads
document.addEventListener('DOMContentLoaded', loadRestaurantData);
```

## 🔧 CORS Configuration

The API is already configured with CORS for frontend development:
- `localhost:3000` (React default)
- `localhost:8080` (Vue default)
- `localhost:4200` (Angular default)
- `127.0.0.1:5500` (Live Server)

## 🎨 Image Handling

All models have default image fallback:
```javascript
const imageUrl = item.image || 'https://safetypreneur.co.id/halaman/kontak-tengah';
```

## 📱 Mobile App Development

The API is also ready for mobile app development:
- React Native
- Flutter
- Ionic
- Native iOS/Android

## 🚀 Production Deployment

When ready for production:
1. Follow steps in `DEPLOYMENT_GUIDE.md`
2. Update API base URL to your domain
3. Test all endpoints on production server

## 🎉 You're All Set!

Your Django Restaurant API is **100% ready** for frontend development. The server is running at `http://localhost:8000/api/` with complete CRUD operations and sample data.

**Happy coding! 🚀**
