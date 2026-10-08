# 🚄 WhooshConnect AI - Smart Transit Ecosystem

WhooshConnect adalah purwarupa sistem **Pusat Kendali Lalu Lintas (TMC) berbasis API** yang dirancang untuk mengatasi *bottleneck* pergerakan *first/last-mile* di kawasan stasiun PT Kereta Cepat Indonesia China (KCIC). 

Sistem ini menerapkan arsitektur 4 Komponen Sistem Transportasi Cerdas (ITS) untuk mengubah manajemen jalan akses yang pasif menjadi ekosistem tertutup (*closed-loop*) yang dinamis.

## 🛠️ Fitur Utama (Loop Detik)
1. **Predictive Fleet Dispatching:** Menganalisis *manifest* penumpang untuk mengirimkan instruksi penambahan armada bus *feeder* secara otomatis sebelum kereta tiba.
2. **Mitigasi Bottleneck VMS:** Mengekstrak data volume dari CCTV untuk memberikan instruksi pengalihan zona penjemputan pada papan VMS.
3. **Parkir Dinamis:** Sinkronisasi ketersediaan slot parkir secara *real-time* ke aplikasi *smartphone* pengguna.

## ⚙️ Arsitektur Sistem
* **Fase 1 (Collect):** Penerimaan data mentah JSON dari Sensor Kamera, GPS Probe, dan Server Tiket.
* **Fase 2 (Process):** Kalkulasi ambang batas kepadatan menggunakan Python FastAPI.
* **Fase 3 (Respond):** *Routing* instruksi ke Aktuator VMS dan Dasbor Armada.

## 🚀 Cara Menjalankan Server Simulasi
1. Pastikan Python terinstal.
2. Instal *framework* FastAPI:
   ```bash
   pip install fastapi uvicorn
