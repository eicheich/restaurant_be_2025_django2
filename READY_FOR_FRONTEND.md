# 🚀 READY FOR FRONTEND!

## Django Restaurant API - Localhost Backend Ready

### ✅ **Setup Complete - API Ready to Use!**

**Server Status:** ✅ Running at `http://localhost:8000/`
**Sample Data:** ✅ 27 menu items + 4 categories loaded
**Images:** ✅ All items have `image-dummy.jpg`

---

## 🎯 **Quick Start untuk Frontend Developer**

### **1. Setup Backend (Once):**
```powershell
# Windows PowerShell
.\start_for_frontend.ps1
```
atau
```bash
# Linux/Mac
./start_for_frontend.sh
```

### **2. Use API Endpoints:**

**Base URL:** `http://localhost:8000/api/`

| Endpoint | Description | Example |
|----------|-------------|---------|
| `GET /api/menu/categories/` | List all categories | [View](http://localhost:8000/api/menu/categories/) |
| `GET /api/menu/items/` | List all menu items | [View](http://localhost:8000/api/menu/items/) |
| `GET /api/articles/` | List all articles | [View](http://localhost:8000/api/articles/) |
| `POST /api/upload/image/` | Upload image | For form uploads |

---

## 📊 **Sample Data Available:**

### **4 Categories:**
1. **Menu Paket** - 2 items (Paket Nila, Sate Kambing)
2. **Minuman** - 8 items (Teh, Jeruk, Kopi, dll)
3. **Menu Makanan** - 7 items (Nila Bakar, Sup Serani, dll)
4. **Cemilan** - 10 items (Mendoan, Tahu Isi, dll)

### **Price Range:** Rp 4,000 - Rp 70,000
### **All Items:** Include `image-dummy.jpg` as placeholder

---

## 💻 **Frontend Implementation:**

```javascript
// Fetch all menu items
const getMenuItems = async () => {
  const response = await fetch('http://localhost:8000/api/menu/items/');
  const items = await response.json();
  return items;
};

// Fetch categories
const getCategories = async () => {
  const response = await fetch('http://localhost:8000/api/menu/categories/');
  const categories = await response.json();
  return categories;
};

// Example item structure:
{
  "id": 1,
  "category": {
    "id": 1,
    "name": "Menu Paket"
  },
  "name": "Paket Nila Bakar/Goreng + Nasi + Es Teh",
  "description": "Paket lengkap nila bakar atau goreng dengan nasi dan es teh",
  "price": "29000.00",
  "image": "http://localhost:8000/media/dummy/image-dummy.jpg",
  "is_available": true
}
```

---

## 🔧 **Development Notes:**

### **CORS:** ✅ Already configured for frontend
### **Media Files:** ✅ Served at `/media/`
### **Admin Panel:** ✅ Available at `/admin/`
### **API Docs:** ✅ DRF browsable API at each endpoint

---

## 📁 **Files untuk Frontend Developer:**

1. **`FRONTEND_API_GUIDE.md`** - Complete API documentation
2. **`start_for_frontend.ps1`** - Quick setup script (Windows)
3. **`start_for_frontend.sh`** - Quick setup script (Linux/Mac)
4. **`requirements.txt`** - Python dependencies

---

## 🚦 **Ready to Start Frontend Development!**

Your Django Restaurant API is now ready as a localhost backend.
Frontend developers can start building the UI and connecting to these endpoints.

**Happy Coding! 🚀**
