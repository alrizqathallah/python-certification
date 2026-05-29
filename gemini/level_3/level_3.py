# # CLASS
# # Membuat "Cetakan" bernama Robot
# class Robot:
#     pass  # pass digunakan sementara jika isi class masih kosong

# # OBJECT
# robot_saya = Robot()  # robot_saya sekarang adalah sebuah Objek

# # Tantangan OOP pertama
# class Mobil:
#     pass

# mobil_iky = Mobil()

# # Contructor
# class Mobil:
#     # Constructor untuk menyiapkan data awal mobil
#     def __init__(self, merek, warna):
#         self.merek = merek  # Menyimpan merek ke dalam mobil ini
#         self.warna = warna  # Menyimpan warna ke dalam mobil ini

# # Sekarang saat mencetak mobil, kita harus memasukkan merek dan warnanya
# mobil_iky = Mobil("Toyota", "Hitam")
# mobil_budi = Mobil("Honda", "Merah")

# # Cara mengakses atributnya
# print(mobil_iky.merek)  # Hasilnya: Toyota
# print(mobil_budi.warna) # Hasilnya: Merah

# Tantangan Constructor dan Atribut
# class Kucing:
#     def __init__(self, nama, ras):
#         self.nama = nama
#         self.ras = ras

# kucing_saya = Kucing("Meong", "Anggora")

# print(f"Kucing saya bernaama {kucing_saya.nama} dan dia adalah ras {kucing_saya.ras}.")


# # Method
# class Kucing:
#     def __init__(self, nama, ras):
#         self.nama = nama
#         self.ras = ras

#     # Ini adalah Method (Perilaku si kucing)
#     def bersuara(self):
#         print(f"{self.nama} berkata: Meong... Miaw!")

# kucing_saya = Kucing("Meong", "Anggora")
# kucing_saya.bersuara()  # Hasil di layar: Meong berkata: Meong... Miaw!

# # Tantangan Method
# class Kalkulator:
#     def tambah(self, angka1, angka2):
#         return angka1 + angka2

# angka1 = int(input("Masukkan angka pertama: "))
# angka2 = int(input("Masukkan angka kedua: "))

# hitung = Kalkulator()

# hasil_penjumlahan = hitung.tambah(angka1, angka2)

# print(f"Hasil penjumlahan dari {angka1} ditambah {angka2} adalah: {hasil_penjumlahan}")


# # INHERITANCE
# # Kelas Induk
# class Hewan:
#     def __init__(self, nama):
#         self.nama = nama

#     def makan(self):
#         print(f"{self.nama} sedang makan... Nyam!")


# # Kelas Anak (Mearisi Hewan)
# class Burung(Hewan):
#     def terbang(self):
#         print(f"{self.nama} terbang tinggi di langit!")


# # Uji Coba
# merpati = Burung("Beni")
# merpati.makan()  # BISA! Warisan dari kelas hewan
# merpati.terbang()  # BISA! Kemampuan unik kelas Burung sendiri

# # Tantangan INHERITANCE
# class Kendaraan:
#     def __init__(self, merek):
#         self.merek = merek

#     def klakson(self):
#         print("Biiip booop!")

# class Motor(Kendaraan):
#     def wheelie(self):
#         print("Motor standing tinggi!")

# roda_dua = Motor("Yamaha")
# print(f"Motor baru saya: {roda_dua.merek}")
# roda_dua.klakson()
# roda_dua.wheelie()

# # POLYMORPHISM
# class Kucing:
#   def bersuara(self):
#     print("Meong!")

# class Anjing:
#   def bersuara(self):
#     print("Guk guk!")

# hewan1 = Kucing()
# hewan2 = Anjing()

# hewan1.bersuara()
# hewan2.bersuara()

# # Tantangan POLYMORPHISM
# class Ovo:
#     def bayar(self, jumlah):
#         print(f"Membayar menggunakan Ovo sebesar Rp {jumlah}")

# class Gopay:
#     def bayar(self, jumlah):
#         print(f"Membayar menggunakan Gopay sebesar Rp {jumlah}")

# pembayaran_ovo = Ovo()
# pembayaran_gopay = Gopay()

# nominal_pembayaran = input("Masukkan nominal pembayaran: ")

# pembayaran_ovo.bayar(nominal_pembayaran)
# pembayaran_gopay.bayar(nominal_pembayaran)


# # ENCAPSULATION
# class AkunBank:
#     def __init__(self, nama, saldo_awal):
#         self.nama - nama
#         self.__saldo = saldo_awal  # Atribut PRIVATE kerena pakai __


# akun_iky = AkunBank("Iky", 50000)

# print(akun_iky.nama)  # BISA diakses: Hasilnya Iky
# print(
#     akun_iky.__saldo
# )  # ERROR! Python akan memproteksinya dan berteriak AttributeError


# # Getter dan Setter
# class AkunBank:
#     def __init__(self, nama, saldo_awal):
#         self.nama = nama
#         self.__saldo = saldo_awal

#     # GETTER: Method untuk mengintip saldo secara aman
#     def cek_saldo(self):
#         return self.__saldo

#     # SETTER: Method untuk mengubah saldo secara aman
#     def isi_saldo(self, jumlah):
#         if jumlah > 0:
#             self.__saldo += jumlah
#         else:
#             print("Jumlah harus lebih dari 0!")


# # Tantangan Encapsulation & Penutup Level 3
# # 1. Membuat Class bernama Akun
# class Akun:
#     def __init__(self, username, password):
#         self.username = username  # Atribut Publik (Bisa diakses siapa saja)
#         self.__password = password  # Atribut Private (Terkunci di dalam kelas)

#     # 2. Membuat Method Getter untuk mengambil data secara aman
#     def lihat_password(self):
#         # Kita bisa menambahkan logika pengecekan di sini jika mau
#         return self.__password


# # 3. Membuat Objek dari kelas Akun
# akun_user = Akun("budi_ganteng", "Rahasia123!")

# # 4. Mencoba mengakses data
# print("Username:", akun_user.username)

# # Mengakses password menggunakan bantuan Getter
# print("Password (via Getter):", akun_user.lihat_password())
