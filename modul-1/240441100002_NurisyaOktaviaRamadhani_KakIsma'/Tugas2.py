class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat
    
    def tampilkan_info(self):
        print(f"Nama      : {self.nama}")
        print(f"NIM       : {self.nim}")
        print(f"Jurusan   : {self.jurusan}")
        print(f"Alamat    : {self.alamat}")
        print("_____________________________")

# Membuat daftar untuk menyimpan objek mahasiswa
mahasiswa_list = []

# Mengambil input untuk 5 mahasiswa
for i in range(5):
    print(f"Masukkan data mahasiswa {i+1}:")
    nama = input("Nama: ")
    nim = input("NIM: ")
    jurusan = input("Jurusan/Prodi: ")
    alamat = input("Alamat: ")
    
    # Membuat objek Mahasiswa
    mahasiswa = Mahasiswa(nama, nim, jurusan, alamat)
    mahasiswa_list.append(mahasiswa)

# Menampilkan informasi semua mahasiswa
tampil_semua = input("Tampilkan semua data mahasiswa? (Ya/Tidak): ")
if tampil_semua == 'Ya':
    for mhs in mahasiswa_list:
        mhs.tampilkan_info()