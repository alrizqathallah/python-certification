# # Membuat fungsi bernama sapa_pengguna
# def sapa_pengguna():
#     print("Halo! Selamat datang di aplikasi kami")


# # Cara memanggil fungsinya:
# sapa_pengguna()

# # Tantangan Fungsi Pertama
# def tampilkan_yell():
#     print("Python itu seru!")

# tampilkan_yell()
# tampilkan_yell()

# # Tantangan Fungsi dengan Parameter dan Return
# def kalikan_angka(angka1, angka2):
#     perkalian = angka1 * angka2
#     return perkalian

# angka1 = input("Masukkan Angka pertama: ")
# angka2 = input("Masukkan Angka kedua: ")
# hasil_perkalian = kalikan_angka(int(angka1),int(angka2))

# print(f"Hasil perkalian {angka1} dengan {angka2} adalah {hasil_perkalian}")

# # Scope
# nama_global = "Iky"  # Ini Global


# def sebuah_fungsi():
#     nama_local = "Bengs"  # Ini Local
#     print(nama_global)  # BISA: Fungsi bisa melihat variabel global


# sebuah_fungsi()
# print(
#     nama_local
# )  # ERROR! Dunia luar tidka kenal nama_local karena dia dikurung didalam fungsi


# # List comprehension
# angka = [1, 2, 3, 4]
# hasil = [x * 2 for x in angka]  # Singkat, padat, jelas!

# # Tangang List comprehension
# harga_asli = [10, 20, 30]
# harga_pajak = [x + 5 for x in harga_asli]

# print(harga_asli)
# print(harga_pajak)

# # File handling
# # 'w' artinya 'write' (menulis/membuat file baru)
# with open("catatan.txt", "w") as file:
#     file.write("Halo, ini isi catatan saya.")

# # 'r' artinya 'read' (membaca file yang sudah ada)
# with open("catatan.txt", "r") as file:
#     isi = file.read()
#     print(isi)

# # Tantangan File Handling
# cerita = input("Masukkan dengan singkat aktivitas anda hari ini: ")

# with open('diary.txt', 'w') as file:
#     file.write(cerita)

# # Error handling
# try:
#     # Kita 'coba' jalankan kode yang berpotensi eror disini
#     angka = int(input("Masukkan angka bulat: "))
#     hasil = 10 / angka
#     print(f"Hasil adalah {hasil}")
# except ValueError:
#     # Blok ini bejalan jika pengguna memasukkan teks, bukan angka
#     print("Error: Yang kamu masukkan bukan angka bulat!")
# except ZeroDivisionError:
#     # Blok ini berjalan jika pengguna memasukkan angak 0 (pembagian dengan nol)
#     print("Error: Angak tidak bisa dibagi dengan nol!")

# # Tantangan Error Handling
# try:
#     def perkalian(angka1, angka2):
#         hitung = angka1 * angka2
#         return hitung

#     angka1 = int(input("Masukkan angka pertama: "))
#     angka2 = int(input("Masukkan angka kedua: "))

#     hasil_perkalian = perkalian(angka1, angka2)

#     print(f"Hasil perkalian dari {angka1} dengan {angka2} adalah {hasil_perkalian}")
# except ValueError:
#     print("Maaf, input harus berupa angka bulat ya!")

# # Modules
# import random

# # Mengambil angka acak bulat antara 1 sampai 10
# angka_acak = random.randint(1, 10)
# print(f"Angka keberuntungan hari ini: {angka_acak}")

# # Tantangan Modul dan Penutup Level 2
# import random

# dadu = random.randint(1, 6)

# print(f"Dadu berputar dan memunculkan angka: {dadu}")

