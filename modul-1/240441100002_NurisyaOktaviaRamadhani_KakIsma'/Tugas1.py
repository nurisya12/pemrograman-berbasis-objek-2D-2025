class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        print(f"{self.nama} sedang berjalan di taman.")

    def berlari(self):
        print(f"{self.nama} sedang berlari di lapangan.")

    def info_manusia(self):
        return f"Nama: {self.nama}, Umur: {self.umur}, Alamat: {self.alamat}"

# Daftar data manusia
data_manusia = [
    ("Ana", 19, "Caruban"),
    ("Vita", 19, "Sumenep"),
    ("Riza", 19, "Lamongan"),
    ("Aisy", 19, "Malang"),
    ("Jihan", 20, "Surabaya")
]

# Membuat objek manusia dan menampilkan informasi
for nama, umur, alamat in data_manusia:
    manusia = Manusia(nama, umur, alamat)
    print(manusia.info_manusia())
    manusia.berjalan()
    manusia.berlari()
    print()