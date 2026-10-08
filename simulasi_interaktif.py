import time

print("==================================================")
print("   SIMULASI PUSAT KENDALI (TMC) WHOOSHCONNECT")
print("==================================================")

# FASE 1: COLLECT (Sistem Meminta Data Lapangan)
print("\n[FASE 1] MEMBACA SENSOR LAPANGAN...")
cctv_kendaraan = int(input("Berapa jumlah kendaraan di area jemput saat ini? : "))
manifest_penumpang = int(input("Berapa jumlah penumpang Whoosh yang turun?     : "))
slot_parkir = int(input("Berapa sisa slot parkir yang kosong?           : "))

# FASE 2: PROCESS (Otak Sistem Menganalisis)
print("\n[FASE 2] AI SEDANG MEMPROSES DATA...")
time.sleep(2) # Memberikan jeda 2 detik agar terlihat seperti sedang berpikir

instruksi_vms = ""
status_feeder = ""
navigasi_app = ""

# Logika 1: Mengurai Bottleneck di VMS
if cctv_kendaraan > 150:
    instruksi_vms = "KAPASITAS PENUH! ARAHKAN MOBIL KE ZONA JEMPUT ALTERNATIF (B)"
elif cctv_kendaraan > 100:
    instruksi_vms = "ANTREAN PADAT. PENGEMUDI DILARANG BERHENTI LAMA (IDLING)"
else:
    instruksi_vms = "ARUS LANCAR. ZONA JEMPUT UTAMA (A) TERSEDIA"

# Logika 2: Menyiapkan Bus Tambahan (Feeder)
if manifest_penumpang >= 500:
    status_feeder = "KRITIS! KIRIM 3 BUS DAMRI TAMBAHAN SEKARANG"
elif manifest_penumpang >= 250:
    status_feeder = "SIAGA! KIRIM 1 BUS DAMRI TAMBAHAN"
else:
    status_feeder = "NORMAL. GUNAKAN JADWAL REGULER"

# Logika 3: Info Parkir ke Ponsel Pengguna
if slot_parkir == 0:
    navigasi_app = "PARKIR STASIUN PENUH. SILAKAN CARI LOKASI LAIN"
else:
    navigasi_app = f"TERSEDIA {slot_parkir} SLOT. NAVIGASI DIAKTIFKAN"

# FASE 3: RESPOND (Sistem Memberikan Keputusan)
print("\n[FASE 3] KEPUTUSAN DIEKSEKUSI (OUTPUT):")
print("--------------------------------------------------")
print(f"🚦 Tampilan Papan VMS Jalan : {instruksi_vms}")
print(f"🚌 Dasbor Operator Bus      : {status_feeder}")
print(f"📱 Notifikasi Aplikasi HP   : {navigasi_app}")
print("==================================================")
