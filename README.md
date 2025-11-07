# 3AWAN Cafe & Resto API (Flask)

API sederhana untuk manajemen menu dan transaksi Cafe & Resto, dibangun dengan Flask.

## Fitur
- Endpoint menu (`/menu`)
- Endpoint transaksi (`/transaction`)
- CORS diaktifkan (mengizinkan akses dari semua origin)

## Struktur Minimal
```
Python-3awan-restocafe/
├─ main.py
├─ config/
│  └─ database.py
└─ routes/
   └─ route.py
```

## Prasyarat
- Python 3.9+ terpasang
- pip terpasang

(Optional) Buat dan gunakan virtual environment:
```bash
python -m venv .venv
# Windows PowerShell
. .venv/Scripts/Activate.ps1
```

Instal dependensi (jika ada `requirements.txt`):
```bash
pip install -r requirements.txt
```

## Menjalankan Secara Lokal
Jalankan aplikasi Flask langsung dari `main.py`:
```bash
python main.py
```
Aplikasi berjalan di:
- URL: http://127.0.0.1:5000
- Host: 0.0.0.0
- Port: 5000

Catatan: Konfigurasi database dikelola di `config/database.py`. Sesuaikan sesuai kebutuhan.

## Endpoint Utama (contoh)
- GET/POST/PUT/DELETE ke resource menu di `/menu` (detail sesuai implementasi di `routes/route.py`)
- Endpoint transaksi di `/transaction`

Silakan lihat isi `routes/route.py` untuk daftar lengkap route dan metode HTTP yang tersedia.

## CORS
CORS telah diaktifkan di `main.py` untuk mengizinkan semua origin:
```python
CORS(app, resources={r"/*": {"origins": "*"}})
```

## Deploy ke Railway
Ada dua cara umum: via GitHub Integration atau Railway CLI.

### 1) Deploy via GitHub Integration
1. Push kode ke GitHub (branch `main`).
2. Di Railway, buat proyek baru atau gunakan yang sudah ada.
3. Hubungkan repo GitHub Anda ke proyek Railway.
4. Railway akan otomatis build dan deploy pada setiap `git push` ke branch yang terhubung.

Start command (contoh):
```bash
python main.py
```

### 2) Deploy via Railway CLI (opsional)
```bash
npm i -g @railway/cli
railway login --browserless
railway link   # pilih project yang benar
railway up     # atau: railway deploy
```

### Domain / Akses dari Ponsel
Jika proyek Anda memiliki domain Railway, akses langsung dari ponsel seperti:
```
[https://<nama-proyek>.up.railway.app](https://python-3awan-api-cafe-resto-production.up.railway.app/menus)
```

## Troubleshooting
- Port bentrok: pastikan tidak ada proses lain di port 5000.
- Dependensi: pastikan `pip install -r requirements.txt` sukses.
- Database: cek `config/database.py` untuk koneksi DB dan izin akses.
- Log Railway: lihat tab Logs pada dashboard Railway untuk error detail.

## Lisensi
Private/Proprietary (ubah sesuai kebutuhan Anda).

