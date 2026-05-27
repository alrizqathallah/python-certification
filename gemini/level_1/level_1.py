# Menampilkan Pesan
print("Iky Benkz")

# Membuat Variabel
nama = "Iky Bengs"  # Menyimpan teks ke dalam varibel bernama 'nama'
usia = 28  # Menyimpan angka ke dalam varibel bernama `usia`

# Tantangan Variabel
kota = "Jakarta Selatan"
jarak = 9.8

print(kota)
print(jarak)

# Input
nama_pengguna = input("Masukkan nama Anda: ")
print("Halo, " + nama_pengguna)

# Tantangan Input
nama = input("Silakan masukkan nama Anda: ")
umur = input("Silakan masukkan usia Anda: ")

print("Halo " + nama + ", usia anda adalah " + umur + " tahun.")

# Melakukan Casting
umur_angka = int(umur)  # Mengubah string "28" menjadi integer 28

# Tantangan konversi data
nama = input("Silakan masukkan nama Anda: ")
umur = input("Silakan masukkan usia Anda saat ini: ")

umur_kedepan = int(umur) + 5

print("Halo, " + nama + "!")
print("Usia kamu saat ini adalah " + umur + " tahun.")
print("Usia kamu 5 tahun depean adalah", umur_kedepan)

# Tantangan Operator
total_tagihan = input("Masukkan total tagihan: ")
jumlah_orang = input("Masukkan jumlah orang: ")

bayar_per_orang = int(total_tagihan) / int(jumlah_orang)

print("Total tagihan per-orang adalah: Rp ", bayar_per_orang)

# Tantangan Perbandingan dan Logika
x = 10
y = 5

# Tebak apa hasil dari 3 baris print ini:
print(x > y)                # True
print(x == y)               # False
print((x > 5) and (y < 3))  # False

# Membuat if, elif, else
nilai = 70

if nilai >= 85:
    print("Nilai kamu A")
elif nilai >= 70:
    print("Nilai kamu B")
else:
    print("Nilai kamu C")

# Tantangan Control Flow
suhu_tubuh = input("Suhu tubuh: ")

batas_suhu = 37.5

if float(suhu_tubuh) >= batas_suhu:
    print("Status: Anda demam, tidak diperbolehkan masuk.")
else:
    print("Status: Suhu normal, silakan masuk!")

# Perulangan For
for i in range(5):
    print("Perulangan ke-", i)

# Perulangan While
hitung = 1

while hitung <= 3:
    print("Angka:", hitung)
    hitung = (
        hitung + 1
    )  # Penting! Agar kondisi suatu saat menjadi False dan perulangan berhenti.

# Tantangan Looping
konter = 5

while konter > 0:
    print(konter)
    konter = konter - 1

print("ROKET MELUNCUR!")

# Membuat List
buah = ["Apel", "Pisang", "Jeruk"]

# Tantangan List
tugas = ["Belajar Python", "Olahraga", "Beli Susu"]

print(tugas[0])

# Tantangan Manipulasi String
produk = "Kopi"
harga = 15000
jumlah = 3

total = harga * jumlah

print(f"Anda membeli {jumlah} {produk} dengan total harga Rp {total}.")