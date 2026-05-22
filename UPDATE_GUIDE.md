# Update Website dan Deploy ke Vercel

## ✅ Yang Sudah Diperbaiki:

1. **Path Assets Diperbaiki**
   - Semua path `../public/` di file root telah diganti menjadi `./public/`
   - File HTML di folder `product/` tetap menggunakan `../public/` (sudah benar)

2. **Gambar yang Tidak Ada Dihapus**
   - Hero image diganti dari `foto landing.png` ke `almond.png`
   - Instagram grid dikurangi dari 5 menjadi 3 gambar (cia1, cia2, cia3)

3. **Konfigurasi Vercel**
   - `vercel.json` sudah dikonfigurasi dengan benar
   - `.vercelignore` sudah dibuat

## 🚀 Cara Push Update ke Vercel:

### Opsi 1: Auto Deploy (Recommended)

```bash
# 1. Cek status file yang berubah
git status

# 2. Add semua perubahan
git add .

# 3. Commit dengan pesan yang jelas
git commit -m "Fix asset paths and Vercel configuration"

# 4. Push ke GitHub
git push origin main
```

**Vercel akan otomatis detect changes dan re-deploy dalam 1-2 menit!**

### Opsi 2: Manual Deploy via CLI

```bash
# Deploy langsung dengan Vercel CLI
vercel --prod
```

## 🔍 Cara Cek Status Deploy:

1. Buka https://vercel.com/dashboard
2. Pilih project `nailsart-web` atau `project-6gmsx`
3. Lihat status deployment di tab "Deployments"
4. Klik deployment terbaru untuk melihat log

## ✨ URL Website Anda:

- **Production**: https://project-6gmsx.vercel.app
- Atau custom domain jika sudah diset

## 🧪 Cara Test Setelah Deploy:

1. Buka website di browser
2. Cek apakah:
   - ✅ Logo ONNAILS muncul di navbar
   - ✅ Hero image (almond nails) muncul
   - ✅ Galeri produk (almond, square, coffin, stilettos) muncul
   - ✅ Video promo muncul
   - ✅ Instagram gallery (3 gambar) muncul
   - ✅ Footer logo dan icon muncul

3. Buka browser console (F12) dan cek apakah ada error 404

## 🐛 Troubleshooting:

### Jika gambar masih tidak muncul:
```bash
# Clear cache Vercel dan re-deploy
vercel --force --prod
```

### Jika perlu cek file struktur di Vercel:
1. Buka deployment di dashboard Vercel
2. Klik tab "Source"
3. Verifikasi folder `public/images` dan `public/video` ada

### Cek error logs:
```bash
# View logs real-time
vercel logs --follow
```

## 📝 File yang Diubah:

1. ✅ `index.html` - Fixed asset paths dan missing images
2. ✅ `vercel.json` - Konfigurasi static hosting
3. ✅ `.vercelignore` - Exclude unnecessary files
4. ✅ `scripts/fix_assets_path.py` - Script otomatis perbaikan path

---

**Next Step:** Jalankan command push di atas untuk update website Anda! 🎉
