                                                                  # **Nebula Scan**

Nebula Scan adalah tools sederhana namun powerful untuk melakukan berbagai tugas jaringan seperti pencarian alamat IP, 
pemindaian port, pemindaian UDP, dan deteksi WAF (Web Application Firewall). Tools ini ditulis dalam Python dan dirancang agar mudah digunakan serta berjalan di Windows, macOS, dan Linux (termasuk Kali Linux).

Fitur
-Cari alamat IP dari hostname
-Scan port otomatis (seperti nmap)
-Scan UDP port otomatis
-Cek apakah domain menggunakan WAF dan mendeteksi jenis WAF
-Hasil scan disimpan ke file (.txt)

Instalation
1. Clone repository dari Github:

```git clone https://github.com/fakhriiazhar/NebulaScan.git```

3. Pindah ke direktori proyek:

```cd Nebula Scan```

4. Buat virtual environment (opsional tapi disarankan):
```
python -m venv venv
source venv/bin/activate  # Linux & macOS
venv\Scripts\activate    # Windows
```

5. install depedencies:

```pip install -r requirements.txt```

6. Jalankan tools:

```python3 Nebula Scan.py```

# **Penggunaan**

Pilih fitur yang tersedia dari menu interaktif:

1 Cari alamat IP dari hostname

2 Scan port otomatis

3 Scan UDP port otomatis

4 Cek apakah domain menggunakan WAF

5 Keluar
