# Troubleshooting: "This site can't be reached"

## Kemungkinan Masalah & Solusi:

### 1. **Python App URL Configuration**
**Problem:** URL aplikasi salah atau belum aktif
**Check:**
- Di cPanel → Python App
- Pastikan Application URL sudah benar (misal: `api`)
- Status aplikasi harus "Running" (hijau)
- Restart aplikasi jika perlu

**Test URL:**
- `yourdomain.com/api/` (bukan `/api/menu-categories/` dulu)
- Harus muncul Django error page atau response, bukan "can't be reached"

### 2. **Application Root Path Salah**
**Problem:** Path folder aplikasi salah
**Check:**
- Application Root harus menuju ke folder project Django
- Contoh: `/home/username/public_html/api/`
- Bukan `/home/username/public_html/api/restaurant_be_2025_django/`

### 3. **passenger_wsgi.py Issue**
**Problem:** WSGI file tidak bisa diload
**Solution:** Test manual di terminal cPanel:
```bash
cd /path/to/your/app
python passenger_wsgi.py
```
Jika error, fix dulu sebelum restart app.

### 4. **Domain/Subdomain Configuration**
**Problem:** Domain belum pointing ke aplikasi
**Check:**
- Apakah pakai subdomain? Pastikan sudah dibuat di cPanel
- Apakah pakai domain utama? Pastikan folder structure benar

### 5. **Port/Firewall Issue**
**Problem:** Server block port atau ada firewall
**Check:**
- Coba akses `yourdomain.com` dulu (tanpa `/api/`)
- Jika domain utama juga ga bisa, masalah di DNS/hosting

### 6. **Django ALLOWED_HOSTS**
**Problem:** Domain belum di-allow
**Fix:** Edit `settings_production.py`:
```python
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

## Quick Debug Steps:

### Step 1: Test Python App Status
1. cPanel → Python App
2. Klik nama aplikasi
3. Check status (harus Running/hijau)
4. Klik "Restart" jika merah

### Step 2: Test Basic URL
- Coba: `yourdomain.com/api/`
- Jangan langsung `/api/menu-categories/`

### Step 3: Check Error Logs
- cPanel → Python App → View Log
- Lihat error terakhir

### Step 4: Test passenger_wsgi.py
```bash
cd /path/to/your/app
python passenger_wsgi.py
```

### Step 5: Update ALLOWED_HOSTS
```python
# settings_production.py
ALLOWED_HOSTS = ['*']  # Sementara untuk testing
```

## Exact URL Pattern:
- ✅ `yourdomain.com/api/`
- ✅ `yourdomain.com/api/menu-categories/`
- ❌ `yourdomain.com/restaurant_be_2025_django/api/`
- ❌ `yourdomain.com:8000/api/`
