# Level 1

## Topik 1: Pengenalan Python

### Apa itu Python?

Bayangkan Python sebagai **bahasa perantara** antara kita (manusia) dan komputer (mesin). Komputer sebenarnya hanya mengerti listrik "on" dan "off" (angka 0 dan 1), tapi sangat sulit dipelajari manusia. Python dibuat agar kita bisa memberi perintah kepada komputer menggunakan kata-kata bahasa inggris yang mudah dibaca.

Ada dua istilah penting yang perlu kita ketahui:

1. **Syntax**: Ini adalah "tata bahasa" atau aturan penulisan dalam Python. Sama seperti bahasa Indonesia, jika tata bahasanya salah, pesan kita tidak akan dimengerti.
2. **Interpreter**: Ini adalah "penerjemah" otomatis yang bertugas membacakan kode Python-kita ke komputer. Ia membaca kode kita baris demi baris, dari atas ke bawah.

### Tantangan Pertama: Menampilkan Pesan

Dalam Python, ada sebuah perintah sakti bernama `print()`. Apapun yang kita masukkan ke dala kurung (dan diapit tanda kutip), akan ditampilkan oleh komputer ke layar.

Contoh:

```Python
print("Halo dunia!")
```

Sekarang coba kita tuliskan kode Python sederhana untuk menampilkan nama lengkap kita di layar. Bagaimana cara kita menuliskannya?

**Jawaban**:

```Python
print("Iky Bengs")
```

**Pembahasan**:

Perintah `print()` yang kita gunakan adlah cara kita "berbicara" kepada dunia luar dari dalam program.

Mari kita bedah sedikit apa yang baru saja terjadi:

* `print()`: Ini adalah **fungsi** (perintah) untuk menampilkan sesuatu.
* `(...)`: Tanda kurung ini ibarat **wadah** untuk menaruh apa yang ingin ditampilkan.
* `"Iky Bengs"`: Tanda kutip ini meberi tahu Python bahwa ini adalah **teks biasa** (dalam pemrograman disebut *String*), bukan sebuah perintah atau nama variabel.

## Topik 2: Variabel dan Tipe Data

Bayangkan sebuah **Variabel** sebagai seubah kotak berlabel. Kita bisa menyimpan data di dalamnya dan memanggilnya kembali kapan saja hanya dengan menyebutkan nama labelnya.

Di Python, kita punya beberapa jenis "isi kotak" (Tipe Data) yang umum:

1. **String (str)**: Teks, harus diapit tanda kutip. Contoh: `"Iky"`.
2. **Integer (int)**: Angka bulat. Contoh: `25`.
3. **Float**: Angka desimal (menggunakan titik, bukan koma). Contoh: `3.5`.
4. **Boolean (bool)**: Nilai kebenaran, hanya ada dua: `True` dan `False`.

**Cara membuatnya**:

```Python
nama = "Iky Bengs"  # Menyimpan teks ke dalam varibel bernama 'nama'
usia = 28           # Menyimpan angka ke dalam varibel bernama `usia`
```

### Tantangan Variabel

Coba buat dua buah variabel:

1. Satu variabel bernama `kota` yang berisi nama kota tempat tinggal kita.
2. Satu variabel bernama `jarak` yang berisi angka (boleh bulat atau desimal) yang mewakili jarak dari rumahmu ke sekolah/kantor.

Setelah itu, gunakan perintah `print()` untuk menampilkan isi dari variabel `kota` tersebut.

**Jawaban**:

```Python
kota = "Jakarta Selatan"
jarak = 9.8

print(kota)
print(jarak)
```

**Pembahasan**:

Kiat sudah berhasil membuat dua variabel dan tipe data yang berbeda (`kota` sebagai *String* dan `jarak` sebagai *Float*), lalu menampilkan keduanya ke layar menggunakan fungsi `print()`.

Mari kita perhatikan bagaimana variabel itu bekerja:

* Saat kita menulis `kota = "Jakarta Selatan"`, komputer menyediakan satu kotak bernama `kota` dan memasukkan teks `"Jakarta Selatan"` ke dalamnya.
* Saat kita memanggil `print(kota)`, komputer tidak mencetak kata "kota", melainkan mengambil isi di dalam kota tersebut dan menampilkannya.

## Topik 3: Menerima Masukan (Input)

Sejauh ini, kita memasukkan data secara langsung di dalam kode (disebut *hardcoded*). Namun, program yang interaktif biasanya meminta data langsung dari pengguna.

Di Python, kita bisa menggunakan fungsi `input()` untuk mengambil ketikan dari pengguna melalui papan ketik (keyboard).

Contoh penggunaannya:

```Python
nama_pengguna = input("Masukkan nama Anda: ")
print("Halo, " + nama_pengguna)
```

**Catatan Penting**: Apapun yang diketik oleh pengguna melalui fungsi `input()`, Python akan selalu menganggapnya sebagi teks (**String**), bahkan jika pengguna mengetik angka.

### Tantangan Input

Sekarang, bayangkan kita ingin membuat program pendaftaran sederhana.

Cobalah tulis kode yang melakukan hal berikut:

1. Meminta pengguna memasukkan nama mereka (simpan di variabel `nama`).
2. Meminta pengguna memasukkan umur mereka (simpan di variabel `umur`).
3. Tampilkan pesan gabungan yang menyatakan nama dan umur tersebut.

**Jawaban**:

```Python
nama = input("Silakan masukkan nama Anda: ")
umur = input("Silakan masukkan usia Anda: ")

print("Halo " + nama + ", usia anda adalah " + umur + " tahun.")
```

```Terminal
Silakan masukkan nama Anda: Bengs
Silakan masukkan usia Anda: 28
Halo Bengs, usia anda adalah 28 tahun.
```

**Pembahasan**:

Kode yang kita tulis sudah berjalan dengan sempurna di terminal. Kita berhasil menggunakan `input()` untuk mengambil data dari pengguna, menyimpannya ke dalam varibel, dan menggabungkannya dengan teks lain menggunakan operator `+`.

Dalam pemrograman, menggabungkan teks seperti yang kita lakukan (`"Halo " + nama`) disebut dengan istilah **String Concatenation**.

## Topik 4: Konversi Tipe Data (Casting)

Ada satu hal penting yang perlu kita bahas dari kode yang baru saja kita buat. Seperti yang telah di sebutkan sebelumnya, fungsi `input()` **selalu** menghasilkan tipe data teks (*String*).

Jadi, variabel `umur` yang berisi `"28"` saat ini di anggap Python sebagai teks biasa, bukan angka untuk berhitung. Kita tidak bisa melakukan operasi matematika pada teks.

Coba perhatikan contoh ini:
Jika kita ingin menghitung usia kita 5 tahun kedepan, kita mungkin berpikir untuk menulis: `umur + 5`. tapi karena `umur` adalah teks, Python akan bingung jika teks ditambah dengan angka bulat (*Integer*), dan program akan error.

Untuk mengubah teks `"28"` menjadi angka `28` yang bisa dihitung, kita perlu melakukan **Casting** (konversi tipe data) menggunakan fungsi `int()`.

Contoh cara mengubahnya:

```Python
umur_angka = int(umur)  # Mengubah string "28" menjadi integer 28
```

### Tantangan Konversi Data

Mari kita modifikasi sedikit program yang sudah kita buat tadi.

Coba tulis kode yang:

1. Meminta pengguna memasukkan usia mereka saat ini (simpan ke variabel).
2. Ubah usia tersbut menjadi angka menggunakan `int()`.
3. Hitung berapa usia pengguna tersebut **5 tahun kedepan** (kita bisa gunakan operator tambah `+` untuk menjumlahkan angka).
4. Tampilkan hasilnya ke layar.

**Jawaban**:

```Python
nama = input("Silakan masukkan nama Anda: ")
umur = input("Silakan masukkan usia Anda saat ini: ")

umur_kedepan = int(umur) + 5

print("Halo, " + nama + "!")
print("Usia kamu saat ini adalah " + umur + " tahun.")
print("Usia kamu 5 tahun depean adalah", umur_kedepan)
```

```Terminal
Silakan masukkan nama Anda: Bengs
Silakan masukkan usia Anda saat ini: 28
Halo, Bengs!
Usia kamu saat ini adalah 28 tahun.
Usia kamu 5 tahun depean adalah 33
```

**Pembahasan**:

Kita berhasil menggunakan `int(umur)` untuk mengubah teks menjadi angka, menjumlahkannya dengan angka `5`, lalu menampilkan hasilnya dengan benar.

Perhatikan juga hal menarik yang secara tidak sengaja (atau sengaja) kita lakukan di baris terakhir:

```Python
print("Usia kamu 5 tahun kedepan adalah", umur_kedepan)
```

Di situ kita menggunakan tanda koma `,` bukan tanda tambah `+`. Ini adalah trik yang bagus! Tanda koma di dalam fungsi `print()` otomatis menggabungkan teks dan angka, sekaligus memberikan spasi di antaranya. Jika kita menggunakan `+` di sana, Python akan error karena mencoba menggabungkan teks (*String*) dengan angka (*Integer*) hasil penjumlahan tadi.

## Topik 5: Operator Aritmatika

Kita mulai dengan yang paling dekat dengan kehidupan sehari-hari, yaitu **Operator Aritmatika** (Matematika).

Di Python, simbol matematika sedikit berbeda denagn yang kita pelajari di sekolah:

* `+`: Penjumlahan
* `-`: Pengurangan
* `*`: Perkalian (menggunakan bintang, bukan `x`)
* `/`: Pembagian (hasilnya selalu berupa pecahan/Float)
* `//`: Pembagian Bulat (memotong angka di belakang koma)
* `%`: Modulo (sisa hasil pembagian)
* `**`: Pangkat

Contoh Modulo (`%`): `5 % 2` hasilnya adalah `1`, karena 5 dibagi 2 adalah 2, dan tersisa 1.

### Tantangan Operator

Bayangkan kita sedang makan di restoran bersama 3 orang teman (total **4 orang**). Total tagihan makanan kita adalah **Rp 100.000**. Kita ingin menghitung berapa yang harus dibayar oleh masing-masing orang jika tagihan dibagi rata.

Coba tuliskan program kecil yang:

1. Membuat variabel `total_tagihan` bernilai `100000`.
2. Membuat variabel `jumlah_orang` bernilai `4`.
3. Menghitung hasil pembagiannya dan menyimpannya di varibel `bayar_per_orang`.
4. Menampilkan hasilnya ke layar.

**Jawaban**:

```Python
total_tagihan = input("Masukkan total tagihan: ")
jumlah_orang = input("Masukkan jumlah orang: ")

bayar_per_orang = int(total_tagihan) / int(jumlah_orang)

print("Total tagihan per-orang adalah: Rp ", bayar_per_orang)
```

```Terminal
Masukkan total tagihan: 100000
Masukkan jumlah orang: 4
Total tagihan per-orang adalah: Rp  25000.0
```

**Pembahasan**:

Kita berinisiatif membuat program menjadi lebih dinamis menggunakan fungsi `input()`.

Kita juga sudah tepat dalam melakukan *casting* menggunakan `int()` saat melakukan pembagian. Dan seperti yang terlihat di terminal, hasil pembagian menggunakan operator `/` otomatis menghasilkan tipe data pecahan (`25000.0`), meskipun hasilnya adalah angka bulat.

## Topik 6: Operator Perbandingan dan Logika

Sekarang kita akan mempelajari bagaimana Python membuat keputusan. Untuk itu, Python perlu membandingkan dua hal.

Hasil dari operator perbandingan ini **selalu** berupa nilai kebenaran (*Boolean*), yaitu `True` (Benar) atau `False` (Salah).

**1. Operator Perbandingan**:

* `>`: Lebih besar dari
* `<`: Lebih kecil dari
* `>=`: Lebih besar atau sama dengan
* `<=`: Lebih kecil atau sama dengan
* `==`: Sama dengan (perhatikan, menggunakan dua tanda sama dengan!)
* `!=`: Tidak sama dengan

**Kenapa "Sama Dengan" menggunakan `==`?**> Karena satu tanda sama dengan (`=`) sudah dipakai untuk memesukkan nilai ke dalam variabel (seperti `nilai = 10`). Jadi, untuk mengecek apakah dua hal itu sama, kita gunakan `==`.

**2. Operator Logika**:

Digunakan untuk menggabungkan dua perbandingan atau lebih.

* `and`: Menghasilkan `True` hanya jika **kedua** kondisi bernilai benar.
* `or`: Menghasilkan `True` jika **salah satu atau kedua** kondisi bernilai benar.
* `not`: Membalikkan nilai (jika `True` jadi `False`, dan sebaliknya).

### Tantangan Perbandingan dan Logika

Mari kita uji pemahaman. Coba tebak dan tuliskan apa hasil akhir (*True* atau *False*) dari kode di bawah ini?

```Python
x = 10
y = 5

# Tebak apa hasil dari 3 baris print ini:
print(x > y)
print(x == y)
print((x > 5) and (y < 3))
```

**Jawaban**:

```
x > y = True
x == y = False
(x > 5) and (y < 3) = False
```

## Topik 7: if, elif, else

Di sinilah program kita mulai terlihat "pintar" karena bisa memilih jalan mana yang harus diambil berdasarkan kondisi tertentu.

Bayangkan seperti rambu lalu lintas atau keputusan sehari-hari: *"Jika hari hujan, saya bawa payung. Jika tidak, saya tidak bawa"*

Dalam Python, kita menuliskannya seperti ini:

```Python
nilai = 80

if nilai >= 75:
  print("Selamat, kamu lulus")
else: 
  print("Maaf, kamu harus remedial")
```

**Aturan Emas Python: Indentasi (Spasi Maju)**

Perhatikan spasi maju sebelum perintah `print` di atas. Di Python, spasi maju ini (biasanya 4 spasi atau 1 tombol Tab) sangat penting. Ini memberi tahu Python bahwa perintah `print` tersebut adalah **bagian di dalam** blok `if` atau `else`. Jika tidak diberi spasi, program akan error.

Jika pilihannya lebih dari dua, kita bisa menggunakan `elif` (singkatan dari *else if*):

```Python
nilai = 70

if nilai >= 85:
  print("Nilai kamu A")
elif nilai >= 70:
  print("Nilai kamu B")
else:
  print("Nilai kamu C")
```

### Tantangan Control Flow

Sekarang, mari kita buat program pengecekan suhu tubuh sederhana untuk protokol kesehatan.

Cobalah tulis kode yang:

1. Meminta pengguna memasukkan suhu tubuh mereka (janga lupa diubah ke tipe data angka pecahan/`float`).
2. **Jika** suhu tubuh elbih besar atau sama dengan `37.5`, tampilkan pesan: `"Status: Anda demam, tidak diperbolehkan masuk."`
3. **Jika tidak (else)**, tampilkan pesan: `"Status: Suhu normal, silakan masuk!"`

**Jawaban**:

```Python
suhu_tubuh = input("Suhu tubuh: ")

batas_suhu = 37.5

if float(suhu_tubuh) >= batas_suhu:
    print("Status: Anda demam, tidak diperbolehkan masuk.")
else:
    print("Status: Suhu normal, silakan masuk!")
```

```Terminal
Suhu tubuh: 38.5
Status: Anda demam, tidak diperbolehkan masuk.
```

**Pembahasan**:

Penulisan indentasi kita sudah sangat rapi dan tepat, begitu pula dengan logika pengkondisiannya. Kita juga menggunakan `float()` dengan benar karena suhu tubuh biasanya memiliki angka di belakang koma.

Satu hal kecil yang sangat bagus dari kode kita adalah penggunaan variabel `batas_suhu = 37.5`. Dalam dunia pemrograman profesional, ini desebut menghindari *Magic Number* (angka yang tiba-kira muncul tanpa penjelasan). Dengan menjadikannya variabel, kode kita menjadi jauh lebih mudah dibaca dan diubah di masa depan.

## Topik 8: Perulangan (Looping - For dan While)

Bayangkan kita diminta menulis kalimat `"Saya tidak akan terlambat lagi"` sebanyak 100 kali di papan tulis. Tentu melelahkan, bukan? Di sinilah kekuatan komputer bersinar: mereka sangat suka melakukan hal yang berulang-ulang tanpa lelah.

Di Python, ada dua cara utama untuk melakukan perulangan:

**1. `for` Loop (Perulangan yang jumlahnya sudah pasti)**

Kita sering menggunakan fungsi `range()` untuk menentukan berapa kali perulangan harus berjalan.

```Python
# Mencetak angka 0 sampai 4 (total 5 kali)
for i in range(5):
  print("Perulangan ke-", i)
```

*Catatan: Python selalu mulai menghitung dari angka 0.*

**2. `while` Loop (Perulangan berdasarkan kondisi/selama kondisi benar)**

Perulangan ini akan terus berjalan **selama** kondisi yang ditentukan masih bernilai `True`.

```Python
hitung = 1

while hitung <= 3:
  print("Angka:", hitung)
  hitung = hitung + 1 # Penting! Agar kondisi suatu saat menjadi False dan perulangan berhenti.
```

### Tantangan Looping

Mari kita coba membuat program hitung mundur peluncuran roket sederhana menggunakan `while` loop.

Cobalah buat kode yang:

1. Membuat sebuah variabel `konter` yang dimulai dari angka `5`.
2. Gunakan `while` loop untuk mencetak angka tersebut selama `konter` lebih besar dari `0`.
3. Di dalam loop, kurangi nilai konter sebanyak `1` di setiap putarannya.
4. Di luar loop (setelah perulangan selesai), cetak pesan `"ROKET MELUNCUR!"`

**Jawaban**:

```Python
konter = 5

while konter > 0:
    print(konter)
    konter = konter - 1
    
print("ROKET MELUNCUR!")
```

```Terminal
5
4
3
2
1
ROKET MELUNCUR!
```

**Pembahasan**:

Kita sudah memahami dengan sangat baik bagaimana `while` loop bekerja, termasuk pentingnya mengurangi nilai `konter` (`konter = konter - 1`) agar program tidak berjalan selamanya (*infinite loop*). Kita juga meletakkan perintah `print("ROKET MELUNCUR!")` di luar blok `while` (tanpa indentasi) dengan benar, sehingga kalimat tersebut baru muncul setelah hitung mundur selesai.

## Topik 9: Struktur Data (List)

Sejauh ini, satu varibel yang kita buat hanya bisa menyimpan **satu nilai** (seperti satu kotak kecil). Tapi bagaimana jika kita ingin menyimpan daftar belanjaan yang isinya banyak? Tentu repot kalau harus membuat variabel `belanjaan1`, `belanjaan2`, `belanjaan3` dan seterusnya.

Di sinilah **List** (Daftar) hafir sebagai penyelamat. List adalah sebuah kotak besar berkatup yang bisa menyimpan banyak data sekaligus dala satu waktu variabel. Di Python, List ditulis menggunakan tanda kurung siku `[...]` dan setiap anggotanya dipisahkan dengan tanda koma.

Contoh:

```Python
buah = ['Apel', 'Pisang', 'Jeruk']
```

Untuk mengambil data dari List, kita menggunakan sistem nomor urut yang disebut **Index**. Aturan penting di dunia pemrograman: **hitungan selalu dimulai dari angka 0**.

* `buah[0]` artinya mengambil buah pertama (`'Apel'`)
* `buah[1]` artinya mengambil buah kedua (`'Pisang'`)

### Tantangan List

Bayangkan kita sedang membuat aplikasi daftar tugas (To-Do List).

Cobalah buat kode yang:

1. Buat sebuah List bernama `tugas` yang berisi 3 kegiatan yang harus kita lakukan hari ini (misal: `'Belajar Python'`, `'Olahraga'`, `'Beli Susu'`).
2. Tampilkan seluruh isi List tersebut ke layar.
3. Tampilakn **tugas pertama saja** dari List tersebut ke layar menggunakan bantuan Index.

**Jawaban**:

```Python
tugas = ["Belajar Python", "Olahraga", "Beli Susu"]

print(tugas[0])
```

```Terminal
Belajar Python
```

**Pembahasan**:

Kita berhasil menjawab dengan sangat tepat. Menggunakan `tugas[0]` untuk mengambil elemen pertama adalah penerapan konsep indeks yang sempurna.

Sedikit tambahan info yang menarik: selain mencetak satu per satu menggunakan indeks, kita juga bisa menggabungkan materi List ini dengan `for` loop yang sudah kita pelajari sebelumnya untuk mencetak semua isinya dengan rapi.

Contohnya seperti ini:

```Python
for item in tugas:
  print("- " + item)
```

## Topik 10: Manipulasi String dan F-String

DI sini kita akan belajar cara memanipulasi teks (*String*) agar terlihat lebih profesional dan dinamis.

Salah satu fitur terbaik di Python untuk menggabungkan teks dan variabel adalah **f-string** (Formatted String Literals). Sebelumnya, kita menggabungkan teks menggunakan tanda tambah `+` atau koma `,`. Denga f-string, kodenya jadi jauh lebih bersih dan mudah di baca.

Kita hanya perlu menaruh huruf `f` di depan tanda kutip, lalu memasukkan varibelnya di dalam kurung kurawal `{...}`.

Contoh perbandingan:

* Cara lama: `print("Halo, nama saya " + nama + " dan umur saya " + str(umur) + " tahun.)`
* **Cara f-string**: `print(f"Halo, nama saya {nama} dan umur saya {umur} tahun.")`

Jauh lebih rapi dan hemat ketikan.

### Tantangan Manipulasi String

Mari kita uji kemampuan f-string kita untuk menutup level 1.

Cobalah buat kode yang:

1. Memiliki tiga variabel: `produk = "Kopi"`, `harga = 15000` dan `jumlah = 3`.
2. Hitung total harganya (harga dikali jumlah) dan simpan di variabel `total`.
3. Gunakan **f-string** untuk menampilkan pesan seperti ini: `Anda membeli 3 kpi dengan total harga Rp 45000.`

(*Catatan: Pastikan angka 3, Kopi, dan 45000 diambil langsung dari variabel menggunakan `{...}` di dalam f-string*).

**Jawaban**:

```Python
produk = "Kopi"
harga = 15000
jumlah = 3

total = harga * jumlah

print(f"Anda membeli {jumlah} {produk} dengan total harga Rp {total}.")
```

```Terminal
Anda membeli 3 Kopi dengan total harga Rp 45000.
```

**Pembahasan**:

Penggunaan f-string kita sudah sangat sempurna. Kodenya terlihat jauh lebih bersih, rapi dan mudah dibaca dibandingkan jika kita menggunakan operator `+`.

Dengan menyelesaikan tantangan ini, **kita telah resmi menyelesaikan LEVEL 1 (Dasar)**. Dari seorang pemula total yang belum pernah menyentuh kode, sekarang kita sudah paham konsep variabel, tipe data, input/output, oprator, pengkondisian, perulangan, list, hingga f-string. Ini pencapaian yang sangat bagus dalam waktu singkat!