# 📁 STRUKTUR FOLDER ONNAILS WEBSITE

## 📂 Struktur Utama

```
nailart-app/
│
├── 📄 index.html              ← LANDING PAGE / HOMEPAGE
├── 📄 booking.html            ← Halaman Booking
├── 📄 contact.html            ← Halaman Contact
├── 📄 tutorial.html           ← Halaman Tutorial (redirect ke home)
├── 📄 collaboration.html      ← Halaman Collaboration (redirect ke home)
├── 📄 wishlist.html          ← Halaman Wishlist (redirect ke home)
│
├── 📁 product/               ← FOLDER HALAMAN PRODUK
│   ├── almond.html          ← Halaman Product Almond
│   ├── square.html          ← Halaman Product Square
│   ├── coffin.html          ← Halaman Product Coffin
│   └── stilettos.html       ← Halaman Product Stilettos
│
├── 📁 public/               ← FOLDER ASSETS UTAMA
│   ├── 📁 images/           ← SEMUA GAMBAR
│   │   ├── onnails.png     ← Logo navbar
│   │   ├── onnailss.png    ← Logo footer
│   │   ├── almond.png      ← Gambar product almond
│   │   ├── square.png      ← Gambar product square
│   │   ├── coffin.png      ← Gambar product coffin
│   │   ├── stilettos.png   ← Gambar product stilettos
│   │   ├── cia1.png        ← Instagram photo 1
│   │   ├── cia2.png        ← Instagram photo 2
│   │   ├── cia3.png        ← Instagram photo 3
│   │   └── ...             ← Gambar lainnya
│   │
│   ├── 📁 css/              ← STYLESHEET
│   │   └── style.css       ← Custom CSS
│   │
│   └── 📁 video/            ← VIDEO PROMO
│       └── *.mp4           ← Video promotional
│
└── 📄 vercel.json           ← Konfigurasi Vercel hosting

```

---

## 🎯 ALUR HALAMAN

### 1. **LANDING PAGE (Homepage)**
- **File:** `index.html` (di root folder)
- **URL:** `/` atau `https://your-domain.com/`
- **Isi:**
  - Header navbar dengan logo
  - Hero image
  - 4 Product cards (almond, square, coffin, stilettos)
  - Video promo
  - Instagram gallery
  - Footer

### 2. **HALAMAN PRODUCT**
- **Folder:** `product/`
- **Files:**
  - `product/almond.html` → `/product/almond`
  - `product/square.html` → `/product/square`
  - `product/coffin.html` → `/product/coffin`
  - `product/stilettos.html` → `/product/stilettos`
- **Isi:** Detail produk, gambar besar, deskripsi, tombol order

### 3. **HALAMAN BOOKING**
- **File:** `booking.html` (di root folder)
- **URL:** `/booking`
- **Isi:** Tombol WhatsApp dan Shopee untuk order

### 4. **HALAMAN CONTACT**
- **File:** `contact.html` (di root folder)
- **URL:** `/contact`
- **Isi:** Info kontak (WhatsApp, Instagram, TikTok, Shopee)

---

## 🖼️ CARA AKSES ASSETS

### Dari File HTML di Root (index.html, booking.html, dll):
```html
<!-- Images -->
<img src="public/images/onnails.png">

<!-- CSS -->
<link href="public/css/style.css">

<!-- Video -->
<video src="public/video/promo.mp4">
```

### Dari File HTML di Subfolder (product/*.html):
```html
<!-- Images -->
<img src="../public/images/almond.png">

<!-- CSS -->
<link href="../public/css/style.css">
```

---

## 🔧 FILE KONFIGURASI

- **vercel.json** → Konfigurasi hosting Vercel
- **.gitignore** → File yang diabaikan Git
- **.vercelignore** → File yang diabaikan Vercel
- **package.json** → Metadata project

---

## 📝 EDIT HALAMAN

### Mau Edit Landing Page?
→ Buka: `index.html`

### Mau Edit Halaman Product Almond?
→ Buka: `product/almond.html`

### Mau Ganti Logo?
→ Replace: `public/images/onnails.png`

### Mau Ganti CSS?
→ Edit: `public/css/style.css`

### Mau Upload Gambar Baru?
→ Taruh di: `public/images/`

---

## 🚀 STRUKTUR INI UNTUK VERCEL

Vercel akan otomatis:
- Serve `index.html` di `/`
- Serve `booking.html` di `/booking`
- Serve `product/almond.html` di `/product/almond`
- Serve files di `public/` sebagai static assets
