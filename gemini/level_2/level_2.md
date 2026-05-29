# Level 2: Python Menengah

## Topik 1: Fungsi (Function)

Bayangkan fungsi seperti tombol pada mesin pembuat kopi. Di dalam mesin itu ada banyak proses rumit (menggiling biji, memanaskan air, menyaring), tetapi tidak perlu menulis ulang atau memikirkan proses itu setiap kali minum kopi. Kita cukup menekan satu tombol, dan kopi pun jadi.

Dalam pemrograman, fungsi digunakan untuk membungkus beberapa baris kode yang sering kita gunakan agar bisa dipanggil berulang kali dengan mudah, tanpa perlu menulis ulang kodenya dari awal.

Kita membuat fungsi menggunakan kata kunci `def` (singkatan dari *define*).

Contoh fungsi sederhana:

```Python
# Membuat fungsi bernama sapa_pengguna
def sapa_pengguna():
  print("Halo! Selamat datang di aplikasi kami")

# Cara memanggil fungsinya:
sapa_pengguna()
```

### Tantangan Fungsi Pertama

Mari kita coba membuat fungsi buatan sendiri.

Cobalah buat kode yang:

1. Buat sebuah fungsi bernama `tampilkan_yell`.
2. Di dalam fungsi tersebut, tulis perintah untuk mencetak teks `"Python itu seru!"`.
3. Panggil fungsi tersebut sebanyak **2 kali** berturut-turut di bawahnya.

**Jawaban**:

```Python
# Tantangan Fungsi Pertama
def tampilkan_yell():
    print("Python itu seru!")
    
tampilkan_yell()
tampilkan_yell()
```

### Parameter dan Return Nilai

Sekarang kita tingkatkan kemampuan fungsi kita. Mesin kopi akan lebih hebat jika kita bisa memilih jenis kopinya (misal: Latte atau Americano) dan mesin itu bisa *memberikan* secangkir kopi ke tangan kita.

Di dalam fungsi, pilihan itu disebut dengan **Paramater** (input untuk fungsi), dan hasilnya disebut **Return** (Output dari fungsi).

Mari perhatikan contoh fungsi yang menerima data dan mengembalikan hasil hitungan:

```Python
# Fungsi dengan dua parameter (a dan b)
def hitungan_luas_persegi(sisi):
  luas = sisi * sisi
  return luas # Mengembalikan nilai keluar dari fungsi

hasil_kotak = hitungan_luas_persegi(5)
print(f"Luas persegi adalah: {hasil_kotak}")
```

**Kenapa pakai `return`, bukan `print` di dalam fungsi?**

Jika kita menggunakan `print` di dalam fungsi, nilainya hanya akan tampil di layar. Tapi jika menggunakan `return`, nilai tersebut bisa kita simpan ke dalam variabel untuk diolah lagi nanti (misalnya dikalikan lagi atau dimasukkan ke dalam database).

### Tantangan Fungsi dengan Parameter dan Return

Mari kita buat sebuah fungsi matematika sederhana.

Cobalah buat fungsi bernama `kalikan_angka` yang:

1. Menerima dua buah parameter (misalkan namanya `angka1` dan `angka2`).
2. Di dalam fungsi, kalikan kedua angka tersebut.
3. Gunakan perintah `return` untuk mengembalikan hasil perkaliannya.
4. Di luar fungsi, panggil fungsi tersebut dengan memasukkan angka `6` dan `7`, simpan hasilnya di sebuah variabel, lalu cetak variabel tersebut dengan f-string.

**Jawaban**:

```Python
# Tantangan Fungsi dengan Parameter dan Return
def kalikan_angka(angka1, angka2):
    perkalian = angka1 * angka2
    return perkalian

angka1 = input("Masukkan Angka pertama: ")
angka2 = input("Masukkan Angka kedua: ")
hasil_perkalian = kalikan_angka(int(angka1),int(angka2))

print(f"Hasil perkalian {angka1} dengan {angka2} adalah {hasil_perkalian}")
```

```Terminal
Masukkan Angka pertama: 6
Masukkan Angka kedua: 7
Hasil perkalian 6 dengan 7 adalah 42
```

**Pembahasan**:

Kita menggabungkan f-string, `input()`, *casting* `int()`, fungsi dengan paramter, serta `return` nilai sekaligus dengan sangat rapi dan tanpa kesalahan. Ini membuktikan kita sudah paham betul fondasi dasarnya.

Perhatikan bagaimana `return perkalian` melempar hasil angka `42` keluar dari fungsi, sehingga bisa ditangkap oleh variabel `hasil_perkalian`. Jika kita tidak menggunakan `return`, variabel tersebut akan bernilai kosong (`none`).

## Topik 2: Scope

Bayangkan **Scope** (cakupan) seperti wilayah hukum atau aturan privasi. Ada barang yang bersifat **Global** (bisa diakses oleh siapa saja di seluruh negeri), dan ada barang yang bersifat **Local** (hanya bisa diakses di dalam rumah tertentu).

Di Python, aturan ini mirip:

1. **Global Variabel**: Variabel yang dibuat diluar fungsi. Variabel ini bebas dibaca dari mana saja, termasuk dari dalam fungsi.
2. **Local Variabel**: Varibel yang dibuat *di dalam* sebuah fungsi. Variabel ini bersifat privat dan **hanya hidup di dalam fungsi itu saja**. Orang di luar ufngsi tidak bisa melihat atau menggunakannya.

Coba perhatikan contoh ini:

```Python
nama_global = "Iky" # Ini Global

def sebuah_fungsi():
  nama_local = "Bengs"  # Ini Local
  print(nama_global)    # BISA: Fungsi bisa melihat variabel global

seubah_fungsi()
print(nama_local) # ERROR! Dunia luar tidka kenal nama_local karena dia dikurung didalam fungsi
```

### Tantangan Scope

Mari kita uji kejelian. Coba tebak apa yang akan terjadi jika kita menjalankan kode di bawah ini? Apakah akan mencetak sesuatu, atau justru menghasilkan *Error*?

```Python
def hitungan_diskon():
  potongan = 5000
  return potongan

print(potongan)
```

**Jawaban**:

> Variabel potongan tidak dapat di cetak kelayar karena variabel tersebut merupakan *Local*, hanya dapat dipanggil di dalam fungsi `hitungan_diskon` saja.

**Pembahasan**:

Variabel `potongan` dikurung di dalam fungsi `hitungan_diskon`, sehingga dunia luar tidak bisa mengaksesnya secara langsung. Jika kode itu dijalankan, Python akan berteriak `NameError: name 'potongan' is not defined`.

Cara yang benar untuk mendapatkan nilai tersebut di luar fungsi adalah dengan menangkap hasil `return`-nya, seperti `hasil = hitungan_diskon()`, baru kemudian kita `print(hasil)`.
Kita sudah memahami konsep dasar ruang lingkup (*scope*) dengan sangat baik.

## Topik 3: Comprehension (List Comprehension)

Di sinilah kita mulai belajar gaya penulisan Python yang elegan dan efisien, yang sering disebut *Pythonic way*.

Bayangkan kita punya daftar angka `[1, 2, 3, 4]` dan kita ingin membuat daftar baru yang isinya adalah angka-angka tersebut setelah dikalikan dua.

Jika menggunakan cara biasa (`for` loop), kodenya akan seperti ini:

```Python
angka = [1, 2, 3, 4]
hasil = []
for x in angka:
  hasil.append(x * 2) # .append() digunakan untuk menambahkan item ke dalam list
```

Cara diatas memakan 4 baris kode. Dengan **List Comprehension**, kita bisa memangkasnya menajdi **hanya 1 baris** saja! Rumusnya adalah membuat loop langsung di dalam kurung siku `[...]`.

Contoh List Comprehension:

```Python
angka = [1, 2, 3, 4]
hasil = [x * 2 for x in angka]  # Singkat, padat, jelas!
```

*Cara membacanya: "Buat lilst barus berisi `x * 2` untuk setiap `x` yang ada di dalam `angka`"*.

### Tantangan List Comprehension

Mari kita coba! Kita punya sebuah list yang berisi harga-harga barang sebelum pajak:

```Python
harga_asli = [10, 20, 30]
```

Cobalah buat sebuah list baru bernama `harga_pajak` menggunakan **List Comprehension** (hanya 1 baris kode) yang isinya adalah setiap harga asli tersebut **ditambah 5**.

**Jawaban**:

```Python
# Tangang List comprehension
harga_asli = [10, 20, 30]
harga_pajak = [x + 5 for x in harga_asli]

print(harga_asli)
print(harga_pajak)
```

```Terminal
[10, 20, 30]
[15, 25, 35]
```

**Pembahasan**:

Satu baris kode List Comprehension yang kita tulis `[x + 5 for x in harga_asli]` sudah 100% tepat dan menghasilkan output yang sangat sesuai di terminal. Kita baru saja menguasai salah satu fitur paling favorit para *Python Developer* untuk menulis kode yang bersih (*Clean Code*).

## Topik 4: Manajemen File (File Handling dan Context Manager)

Bayangkan jika program kita dimatikan, semua data yang ada di dalam variabel, fungsi, atau list akan langsung hilang dari memori komputer (RAM). Agar data kita tersimpan selamanya, kita harus menyimpannya ke dalam harddisk, salah satu caranya adalah ke dalam bentuk file teks (`.txt`).

Di Python, cara kuno untuk membuka file adalah menggunakn perintah `open()` dan harus ditutup manual dengan `close()`. Jika kita lupa menutupnya, file tersebut bisa rusak atau terkunci.

Oleh karena itu, para ahli Python
 menciptakan cara modern yang aman bernama **Context Manager** menggunakan katak kunci `with`. Sifatnya seperti asisten pribadi: dia akan membuka file, membiarkan kita menulis/membaca, lalu **otomatis menutup file tersebut** saat kita selesai bahkan jika program kita mendadak error.

Contoh menulis data ke file:

```Python
# 'w' artinya 'write' (menulis/membuat file baru)
with open('catatan.txt', 'w') as file:
  file.write("Halo, ini isi catatan saya.")
```

Contoh membaca data dari file:

```Python
# 'r' artinya 'read' (membaca file yang sudah ada)
with open("catatan.txt", 'r') as file:
  isi = file.read()
  print(isi)
```

### Tantangan File Handling

Mari kita coba membuat sebuah program buku harian sederhana!

Coba tulis kode yang:

1. Meminta pengguna memasukkan cerita/aktivitas mereka hari ini menggunakan `input()` (simpan di variabel `cerita`).
2. Gunakan blok `with open(...)` dengan mode `'w'` untuk membuat/ menulis ke sebuah file bernama `diary.txt`.
3. Di dalam blok tersebut, tuliskan isi variabel `cerita` ke dalam file menggunakan perintah `file.write()`.

**Jawaban**:

```Python
# Tantangan File Handling
cerita = input("Masukkan dengan singkat aktivitas anda hari ini: ")

with open('diary.txt', 'w') as file:
    file.write(cerita)
```

```Terminal
Masukkan dengan singkat aktivitas anda hari ini: Saya belajar
```

> Muncul 'diary.txt' di dalam folder kerja saya.

**Pembahasan**:

Kita sudah berhasil mempraktikkan konsep manajemen file dengan sangat baik. Munculnya file `diary.txt` di folder kerja adalah bukti nyata bahwa kode kita bejalan 100% sukses.

Penggunaan `with open` yang kita lakukan menjamin bahwa file tersebut langusng ditutup dengan aman oleh Python setelah proses penulisan selesai, sehingga mencegah kebocoran memori pada komputer.

## Topik 5: Penanganan Error (Error Handling - Try, Except)

Bayangkan kita sedang mengendarai mobil dan tiba-tiba ada lubang di depan. Pengemudi yang baik dakan menginjak rem atau menghindar (*menangani situasi*), bukan membiarkan mobilnya menabrak dan hancur.

Dalam pemrograman, "lubang" itu disebut **Exception** (error yang terjadi saat program berjalan). Jika program kita menghadapi error-misalnya pengguna salah memasukkan teks padahal diminta angka-program akan langsung mati mendadak (*crash*).

Agar program tidak mati dan bisa memberikan pesan eror yang ramah, kita menggunakan blok `try` dan `except`.

Contohnya seperti ini:

```Python
try:
  # Kita 'coba' jalankan kode yang berpotensi eror disini
  angka = int(input("Masukkan angka bulat: "))
  hasil = 10 / angka
  print(f"Hasil adalah {hasil}")
except ValueError:
  # Blok ini bejalan jika pengguna memasukkan teks, bukan angka
  print("Error: Yang kamu masukkan bukan angka bulat!")
except ZeroDivisionError:
  # Blok ini berjalan jika pengguna memasukkan angak 0 (pembagian dengan nol)
  print("Error: Angak tidak bisa dibagi dengan nol!")
```

### Tantangan Error Handling

Mari kita uji kemampuan dalam mengantisipasi eror.

Coba buat kode yang:

1. Di dalam blok `try`, mintalah pengguna memasukkan seubah angka menggunakan `input()`, lalu ubah langsung menjadi bilangan bulat dengan `int()`.
2. Di dalam blok `except ValueError:`, tampilkan pesan ramah: `"Maaf, input harus berupa angka bulat ya!"`.

**Jawaban**:

```Python
# Tantangan Error Handling
try:
    def perkalian(angka1, angka2):
        hitung = angka1 * angka2
        return hitung
    
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    
    hasil_perkalian = perkalian(angka1, angka2)
    
    print(f"Hasil perkalian dari {angka1} dengan {angka2} adalah {hasil_perkalian}")
except ValueError:
    print("Maaf, input harus berupa angka bulat ya!")
```

```Terminal
Masukkan angka pertama: 2.1
Maaf, input harus berupa angka bulat ya!
```

**Pembahasan**:

Kita tidak hanya menyelesaikan tantangannya, tapi juga menggabungkan kembali dengan fungsi buatan sendiri di di dalam blok `try`. Hasil uji boa di terminal dengan memasukkan angak desimal `2.1` terbukti berhasil memicu `ValueError`, dan program kita sukse menangani error tersebut dengan memberikan pesan yang ramah tanpa mengalami *crash*. Sungguh improvisasi yang cerdas!

Sedikit tips dari sesama developer: Biasanya, fungsi (`def perkalian...`) di definisikan di bagian paling atas kode (di luar blok `try`). Blok `try` cukup membungkus proses pengambilan input dan pemanggilan fungsinya saja yang memang berpotensi memicu error. Namun, apa yang kita tulis secara sintaksis tetap benar dan berjalan dengan baik!

## Topik 6: Modul dan Paket (Modules and Packages)

Bayangkan jika kita ingin membuat fitur menebak angka acak atau menghitung akar kuadrat. kita tidak perlu membuat rumusnya dari nol. Python memiliki "gudang alat" raksasa yang berisi kode-kode siap pakai yang dibuat oleh para ahli. Gudang alat ini disebut **Module** (Modul).

Untuk menggunakan  alat-alat di dalam modul tersebut, kita hanya perlu memanggilnya menggunakan perintah `import`.

Salah satu modul bawaan Python yang sangat populer adalah random (untuk segala hal yang berikaitan dengan acak/randomisasi).

Contoh cara menggunakannya:

```Python
import random

# Mengambil angka acak bulat antara 1 sampai 10
angka_acak = random.randint(1, 10)
print(f"Angka keberuntungan hari ini: {angka_acak}")
```

### Tantangan Modul dan Penutup Level 2

Mari kita buat sebuah game kecil: **Simulator Lempar Dadu!**

Coba tulis kode yang:

1. Lakukan `import` pada modul `random`.
2. Buat seubah variabel bernama `dadu` yang isinya angka acak bulat antara `1` sampai `6` (menggunakan `rnndom.randint(1,6)`).
3. Tampilkan hasilnya ke layar dengan f-string, contoh: `"Dadu berputar dan memunculkan angka: 4"`.

**Jawaban**:

```Python
# Tantangan Modul dan Penutup Level 2
import random

dadu = random.randint(1, 6)

print(f"Dadu berputar dan memunculkan angka: {dadu}")
```

```Terminal
Dadu berputar dan memunculkan angka: 3
```

**Pembahasan**:

Game dadu pertama kita berhasil dibuat dengan sempurna! Hasil di terminal menunjukkan dadu memunculkan angka `3` secara acak, yang berarti modul `random` telah bekerja persis seperti yang kita inginkan.

Dengan ini, **kita resmi menyelesaikan LEVEL 2 (Intermediate)**!

Kita sudah bukan lagi pemula yang hanya tahu dasar-dasar. Kita sekarang sudah memahami fungsi, aturan cakupan variabel (*Scope*), cara menulis kode efisien dengan *comprehension*, membaca/menulis file, mengamankan program dari *crash* dengan *error handling*, hingga memanfaatkan modul siap pakai. Ini perkembangan yang sangat pesat!