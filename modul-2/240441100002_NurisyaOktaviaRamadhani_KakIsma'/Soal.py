class MataKuliah:
    def __init__(self, kode, nama, sks):
        valid = sks == 2 or sks == 3
        if valid:
            self.sks = sks
        else:
            print("SKS tidak valid, default 2 SKS digunakan.")
            self.sks = 2
        self.kode = kode
        self.nama = nama


class Mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        panjang = len(nim)
        awal = nim[:2]
        semua_angka = nim.isdigit()

        if awal == "23" and panjang == 10 and semua_angka:
            self.nim = nim
        else:
            print("NIM tidak valid, gunakan default.")
            self.nim = "2300000000"

        self.nama = nama
        self.prodi = prodi
        self.matkul = []
        Mahasiswa.total_mahasiswa += 1

    def tambah_matkul(self, mk):
        self.matkul.append(mk)

    def tampilkan(self):
        print("\nMahasiswa :", self.nama)
        print("NIM         :", self.nim)
        print("Prodi       :", self.prodi)
        print("Mata Kuliah :")
        for m in self.matkul:
            print("-", m.nama, "(", m.kode, ")", "|", m.sks, "SKS")

        if len(self.matkul) < 4:
            print(">>> Peringatan: Mata kuliah yang diambil kurang dari 4!")

    @classmethod
    def jumlah(cls):
        print("\nTotal Mahasiswa:", cls.total_mahasiswa)


class Kampus:
    total_mahasiswa = 0

    def __init__(self, nama, alamat):
        angka_ada = any(huruf.isdigit() for huruf in nama)
        if angka_ada:
            print("Nama kampus tidak valid, diganti ke default.")
            self.nama = "Kampus Default"
        else:
            self.nama = nama
        self.alamat = alamat

    @classmethod
    def tampil(cls, nama, alamat):
        print("\nNama Kampus    :", nama)
        print("Alamat Kampus  :", alamat)
        print("Total Mahasiswa:", cls.total_mahasiswa)


# DATA MATAKULIAH
mk1 = MataKuliah("IF001", "PBO", 3)
mk2 = MataKuliah("IF002", "B. Inggris", 3)
mk3 = MataKuliah("IF003", "E-Business", 3)
mk4 = MataKuliah("IF004", "PAI", 2)
mk5 = MataKuliah("IF005", "PBW", 4)  # invalid
mk6 = MataKuliah("IF006", "DMJ", 3)
mk7 = MataKuliah("IF007", "PBD", 2)
mk8 = MataKuliah("IF008", "APB", 3)

# DATA MAHASISWA
m1 = Mahasiswa("Okta", "2312345678", "Informatika")
m1.tambah_matkul(mk1)
m1.tambah_matkul(mk2)
m1.tambah_matkul(mk3)
m1.tambah_matkul(mk4)

m2 = Mahasiswa("Aisy", "2312345679", "SI")
m2.tambah_matkul(mk2)
m2.tambah_matkul(mk5)
m2.tambah_matkul(mk6)
m2.tambah_matkul(mk7)

m3 = Mahasiswa("Jihan", "2312345680", "TI")
m3.tambah_matkul(mk1)
m3.tambah_matkul(mk2)
m3.tambah_matkul(mk3)


m4 = Mahasiswa("Riza", "2312345681", "SI")
m4.tambah_matkul(mk5)
m4.tambah_matkul(mk6)
m4.tambah_matkul(mk7)
m4.tambah_matkul(mk8)

m5 = Mahasiswa("Vita", "2312345682", "TI")
m5.tambah_matkul(mk1)
m5.tambah_matkul(mk2)
m5.tambah_matkul(mk3)
m5.tambah_matkul(mk4)

m6 = Mahasiswa("Ana", "1234567890", "Informatika")  # NIM invalid
m6.tambah_matkul(mk1)
m6.tambah_matkul(mk6)
m6.tambah_matkul(mk7)


# TAMPILKAN MAHASISWA
m1.tampilkan()
m2.tampilkan()
m3.tampilkan()
m4.tampilkan()
m5.tampilkan()
m6.tampilkan()

Mahasiswa.jumlah()

# DATA KAMPUS
kampus = Kampus("Universitas Trunojoyo Madura", "Jl. Telang")
Kampus.total_mahasiswa = Mahasiswa.total_mahasiswa
Kampus.tampil(kampus.nama, kampus.alamat)
