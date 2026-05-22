# Panduan Deploy ke Vercel - ONNAILS

## Cara 1: Deploy melalui Website Vercel (Paling Mudah)

### Langkah-langkah:

1. **Buka website Vercel**
   - Kunjungi https://vercel.com
   - Login atau Sign up dengan akun GitHub/GitLab/Bitbucket

2. **Import Project**
   - Klik tombol **"Add New..."** → **"Project"**
   - Pilih **"Import Git Repository"**
   - Authorize Vercel untuk mengakses repository Anda
   - Pilih repository `nailart-app`

3. **Configure Project**
   - **Project Name**: `onnails` (atau nama yang Anda inginkan)
   - **Framework Preset**: `Other` (biarkan default)
   - **Root Directory**: `./` (biarkan default)
   - **Build Command**: (kosongkan - tidak perlu)
   - **Output Directory**: `./` (biarkan default)
   - **Install Command**: (kosongkan - tidak perlu)

4. **Deploy**
   - Klik tombol **"Deploy"**
   - Tunggu beberapa detik sampai proses selesai
   - Website Anda akan live di URL: `https://nama-project.vercel.app`

---

## Cara 2: Deploy via Command Line (CLI)

### Persiapan:
```bash
# Install Vercel CLI
npm install -g vercel
```

### Deploy:
```bash
# Masuk ke folder project
cd c:\data azril\nailart-app

# Login ke Vercel (akan membuka browser)
vercel login

# Deploy project
vercel

# Ikuti prompt:
# - Set up and deploy? → Yes
# - Which scope? → Pilih account Anda
# - Link to existing project? → No
# - What's your project's name? → onnails
# - In which directory is your code located? → ./
```

### Deploy Production:
```bash
# Deploy ke production URL
vercel --prod
```

---

## Troubleshooting

### Masalah CSS/Images Tidak Muncul:
- Pastikan path di HTML menggunakan path relatif
- Contoh: `../public/css/style.css` atau `./public/images/photo.jpg`

### Update Website:
```bash
# Setiap kali ada perubahan, jalankan:
git add .
git commit -m "Update website"
git push

# Vercel akan otomatis re-deploy
# Atau jalankan manual:
vercel --prod
```

### Custom Domain:
1. Buka dashboard Vercel
2. Pilih project Anda
3. Klik **Settings** → **Domains**
4. Tambahkan domain Anda
5. Update DNS settings sesuai instruksi Vercel

---

## File Penting untuk Deployment

✅ **vercel.json** - Sudah dikonfigurasi
✅ **.vercelignore** - Sudah dibuat
✅ **package.json** - Sudah ada

## URL Setelah Deploy
Setelah berhasil deploy, website Anda akan tersedia di:
- Development: `https://nama-project-hash.vercel.app`
- Production: `https://nama-project.vercel.app`

## Status Check
Cek status deployment Anda di: https://vercel.com/dashboard
