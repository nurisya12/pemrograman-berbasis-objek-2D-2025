class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 5

class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, jenis_kendaraan):
        Pengiriman.__init__(self, asal, tujuan)
        self.jenis_kendaraan = jenis_kendaraan

    def estimasi_waktu(self):
        if self.jenis_kendaraan == "Truk":
            return 6
        elif self.jenis_kendaraan == "Motor":
            return 4
        else:
            return Pengiriman.estimasi_waktu(self)

class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai == "Garuda":
            return 2
        elif self.maskapai == "Lion Air":
            return 3
        else:
            return Pengiriman.estimasi_waktu(self)

class PengirimanInternasional(PengirimanDarat, PengirimanUdara):
    def __init__(self, asal, tujuan, jenis_kendaraan, maskapai):
        Pengiriman.__init__(self, asal, tujuan)   # panggil Pengiriman langsung
        self.jenis_kendaraan = jenis_kendaraan
        self.maskapai = maskapai

    def estimasi_waktu(self):
        # Utamakan estimasi dari Udara
        if self.maskapai == "Garuda":
            waktu = 2
        elif self.maskapai == "Lion Air":
            waktu = 3
        else:
            waktu = 5

        # Kalau tujuan bukan Indonesia, tambah 3 hari
        if self.tujuan != "Indonesia":
            waktu += 3
        return waktu

# Membuat beberapa objek
pengiriman1 = PengirimanInternasional("Jakarta", "Malaysia", "Truk", "Garuda")
pengiriman2 = PengirimanInternasional("Surabaya", "Indonesia", "Motor", "Lion Air")
pengiriman3 = PengirimanInternasional("Medan", "Singapura", "Truk", "Lion Air")

# Menampilkan estimasi waktu
print(f"Estimasi pengiriman 1: {pengiriman1.estimasi_waktu()} hari")
print(f"Estimasi pengiriman 2: {pengiriman2.estimasi_waktu()} hari")
print(f"Estimasi pengiriman 3: {pengiriman3.estimasi_waktu()} hari")