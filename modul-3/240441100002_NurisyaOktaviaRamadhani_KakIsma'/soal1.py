class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama: {self.nama}, Gaji: {self.gaji}, Departemen: {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        print(f"[Karyawan Tetap] Nama: {self.nama}, Gaji: {self.gaji}, Departemen: {self.departemen}, Tunjangan: {self.tunjangan}")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        print(f"[Karyawan Harian] Nama: {self.nama}, Gaji: {self.gaji}, Departemen: {self.departemen}, Jam Kerja: {self.jam_kerja} jam/hari")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, karyawan):
        self.daftar_karyawan.append(karyawan)

    def tampilkan_semua_karyawan(self):
        for karyawan in self.daftar_karyawan:
            karyawan.info()

# Membuat objek manajemen karyawan
manajemen = ManajemenKaryawan()

# Menambahkan beberapa karyawan tetap dan harian
karyawan1 = KaryawanTetap("Andi", 5000000, "IT", 1000000)
karyawan2 = KaryawanTetap("Budi", 5500000, "HRD", 1200000)
karyawan3 = KaryawanHarian("Cici", 150000, "Operasional", 8)
karyawan4 = KaryawanHarian("Dina", 160000, "Marketing", 7)

manajemen.tambah_karyawan(karyawan1)
manajemen.tambah_karyawan(karyawan2)
manajemen.tambah_karyawan(karyawan3)
manajemen.tambah_karyawan(karyawan4)

# Menampilkan semua karyawan
manajemen.tampilkan_semua_karyawan()