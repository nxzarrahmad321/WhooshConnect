"""
=========================================================
WHOOSHCONNECT TMC (TRAFFIC MANAGEMENT CENTER) API
Sistem Transportasi Cerdas - Integrasi Antarmoda PT KCIC
=========================================================
Author: Nazar Ahmad Harris
Program: D-III Manajemen Transportasi Jalan
"""

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

# 1. Inisialisasi Server Otak TMC
app = FastAPI(
    title="WhooshConnect TMC API",
    description="Saraf digital untuk prediksi antrean dan manajemen armada stasiun KCIC.",
    version="1.0.0"
)

# 2. Skema Data dari Sensor (Input - Fase 1)
class SensorLapangan(BaseModel):
    id_stasiun: str
    volume_cctv_penjemput: int
    jumlah_manifest_turun: int
    sisa_slot_parkir: int

# 3. Logika Analisis & Keputusan (Process - Fase 2)
@app.post("/api/v1/analisis-pergerakan")
async def proses_lalu_lintas(data: SensorLapangan):
    waktu_deteksi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Inisialisasi Output Kosong
    keputusan = {
        "waktu_sistem": waktu_deteksi,
        "instruksi_vms": "",
        "status_feeder": "",
        "navigasi_pengguna": ""
    }

    # A. Modul Mitigasi Bottleneck (Aktuator VMS)
    if data.volume_cctv_penjemput > 150:
        keputusan["instruksi_vms"] = "[KAPASITAS MAX] ARAHKAN KE ZONA JEMPUT B (ALTERNATIF)"
    elif data.volume_cctv_penjemput > 100:
        keputusan["instruksi_vms"] = "[PADAT] SIAPKAN KENDARAAN, DILARANG IDLING"
    else:
        keputusan["instruksi_vms"] = "[LANCAR] ZONA JEMPUT A TERSEDIA"

    # B. Modul Predictive Fleet Dispatching (Bus DAMRI/Feeder)
    if data.jumlah_manifest_turun >= 500:
        keputusan["status_feeder"] = "DISPATCH CRITICAL: KIRIM 3 BUS TAMBAHAN"
    elif data.jumlah_manifest_turun >= 250:
        keputusan["status_feeder"] = "DISPATCH WARNING: KIRIM 1 BUS TAMBAHAN"
    else:
        keputusan["status_feeder"] = "STANDBY: JADWAL REGULER"

    # C. Modul Parkir Dinamis (Aplikasi Ponsel)
    if data.sisa_slot_parkir == 0:
        keputusan["navigasi_pengguna"] = "PARKIR PENUH - ARAHKAN KE PARKIR TRANSIT"
    else:
        keputusan["navigasi_pengguna"] = f"TERSEDIA {data.sisa_slot_parkir} SLOT - NAVIGASI AKTIF"

    # 4. Transmisi ke Aktuator (Output - Fase 3)
    return {
        "status": "success",
        "pesan": f"Analisis loop detik selesai untuk {data.id_stasiun}",
        "eksekusi": keputusan
    }
