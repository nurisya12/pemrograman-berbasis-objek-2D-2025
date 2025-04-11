class Kucing:
    def __init__(self, nama): 
        self.nama = nama
    
    def info(self):
        print(f"{self.nama} berbunyi: Meong!")
        print(f"{self.nama} makan ikan.")

class Burung:
    def __init__(self, nama): 
        self.nama = nama
    
    def info(self):
        print(f"{self.nama} berkicau: Cuit cuit!")
        print(f"{self.nama} terbang di langit.")

class Ikan:
    def __init__(self, nama): 
        self.nama = nama
    
    def info(self):
        print(f"{self.nama} berenang di air.")
        print(f"{self.nama} makan pelet ikan.")

# Urutan jenis hewan yang diinginkan
jenis_hewan = [Kucing, Burung, Ikan, Kucing, Burung]

hewan_list = []
nomor = 1
for Jenis in jenis_hewan:
    nama = f"{Jenis.__name__}-{nomor}" 
    hewan = Jenis(nama)
    hewan_list.append(hewan)
    nomor += 1

for hewan in hewan_list:
    print("___________")
    print(f"Hewan: {hewan.nama}")
    hewan.info()