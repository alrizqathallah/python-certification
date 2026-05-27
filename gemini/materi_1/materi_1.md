# Materi 1: Python Dasar (Fundamental)

## 1. Apa itu Python

Bayangkan Python sebagai sebuah bahasa untuk memberi perintah kepada komputer. Berbeda dengan bahasa mesin yang rumit, Python dirancang agar mudah dibaca oleh manusia-hampir seperti bahasa inggris sederhana.

* **Sejarah Singkat**: Diciptakan oleh **Guido Van Rossum** pada tahun 1991. Nama "Python" diambil dari grup komedi favoritnya, *Monty Python*.
* **Kegunaan**: Python ada di mana-mana! Mulai dari membuat website (Instagram/YouTube), analisis data, kecerdasan buatan (AI), hingga otomatisasi tugas kantor yang membosankan.
* **Interpreter**: Python adalah bahasa *interpreted*. Artinya, ada sebuah program (disebut Interpreter) yang membaca kode kita baris demi baris dan langsung menjalankannya.

## 2. Varibel dan Tipe Data Dasar

Mari kita mulai dengan konsep paling dasar dalam pemrograman: **Variabel**.

**Analogi**: Bayangkan variabel sebagai sebuah **kotak** yang memiliki **label** (nama) di luarnya. Kita bisa menyimpan **sesuatu** (data) di dalam kotak tersebut untuk digunakan nanti.

Di Python, kita punya beberapa tipe "isi kotak" yang sering digunakan:

| Tipe Data | Nama di Python | Penjelasan | Contoh |
|-----------|----------------|------------|--------|
| **Integer** | `int` | Bilangan bulat (positif/negatif) | `10`, `-5`, `0` |
| **Float** | `float` | Bilangan desimal (positif/negatif) | `3.14`, `2.0` |
| **String** | `str` | Teks (diapit tanda kutip) | `"Halo"`, `'Python'` |
| **Boolean** | `bool` | Nilai kebenaran | `True`, `False` |

## Contoh Kode:

```python
# Membuat variabel
nama = "Budi"       # String
umur = 20           # Integer
tinggi = 175.5      # Float
is_pelajar = True   # Boolean

# Menampilkan isi varibel ke layar
print(nama)
print(umur)
```

**Catatan Penting**: Di Python, nama varibel tidak boleh diawali angka dan tidak boleh ada spasi (gunakan `_` sebagai pengganti spasi, contoh: `nama_saya`).

## Latihan

Jika kita ingin membuat program untuk menyimpan data sebuah **toko buku**, tipe data apa yang paling cocok digunakan untuk menyimpan:

1. **Nama Buku**?
2. **Harga Buku** (misal: 50000)?
3. **Rating Buku** (misal: 4.8)?
4. **Apakah buku tesebut masih tersedia**? (Ya/Tidak)

## Jawaban

Untuk **Nama Buku** menggunakan tipe data *String*, **Harga Buku** menggunakan *Integer*, **Rating Buku** menggunakan *Float*, dan **Ketersediaan Buku** menggunaakn *Boolean*.

```python
nama_buku = "Pemrograman Python"
harga_buku = 50000
raing_buku = 4.8
buku_tersedia = True
```


