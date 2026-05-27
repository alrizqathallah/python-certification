# Materi 1

## 1.1 Pengenalan Python

### Apa itu Python?

**Python** adalah bahasa pemrograman yang:
* Mudah dibaca dan dipelajari (mirip bahasa manusia)
* Digunakan di banyak bidang:
  * Web Development
  * Data Science
  * AI / Machine Learning
  * Automation
  * Game (Basic)

**Analogi**:

Python itu seperti bahasa inggris untuk komputer.
Kalau kita bisa "bicara Python", kita bisa kasih perintah ke komputer.

### Bagaimaan Python Bekerja?

Python menggunakan **interpreter**

Artinya:

*  Kode kita dibaca **baris per baris**.
*  Langsung dijalankan.

Berbeda dengan bahasa seperti *C* yang harus dikompilasi dulu.

### Contoh Pertama (Hello World)

Ini program python paling sederhana:

```python
print("Hello, World!")
```

**Penjelasan**:

* `print()` = perintah untuk menampilkan sesuatu ke layar
* `"Hello World!"` = teks yang ingin ditampilkan

**Output**:

```terminal
Hello, World!
```

### Konsep Penting Pertama

Dalam Python:

* Setiap baris = instruksi
* Tidak perlu tanda `;`
* Penulisan harus rapi (indentasi penting nanti)

### Latihan 1 (Super Basic)

**Soal**:

Apa output dari kode berikut?

```python
print("Halo")
print("Saya belajar Python")
```

### Latihan 2

Tulis kode Python untuk menampilkan:

```python
Nama saya budi
Saya suka belajar koding
```

### Mini Challenge

Buat program yang menampilkan:

```
=== BIODATA ===
Nama: (nama)
Umur: (umur)
```

Contoh:

```
=== BIODATA ===
Nama: Andi
Umur: 20
```

### Jawban

Output Latihan 1:

```terminal
Halo
Saya belajar Python
```

Kode Latihan 2:

```python
print("Nama saya Budi")
print("Saya suka belajar coding")
```

Mini Challenge:

```python
print("=== BIODATA ===")
print("Nama: Bengs")
print("Umur: 28")
```

```terminal
=== BIODATA ===
Nama: Bengs
Umur: 28
```

### Insight Penting

Tanpa sadar kita sudah paham:

* Cara menjalankan perintah Python
* Fungsi `print()`
* Output multi baris
* Format teks sederhana

---

## 1.2 Varibel dan Tipe Data

### Apa itu Variabel?

Variabel itu seperti **kotak penyimpanan**.

**Ananlogi**:

Bayangkan kita punya kota berlabel:

* `nama`
* `umur`

Di dalamnya kita bisa isi data.

### Contoh Variabel

```python
nama = "Bengs"  # String
umur = 28       # Integer
```

**Penjelasan**:

* `nama` -> variabel
* `"Bengs"` -> isi data (string)
* `umur` -> variabel
* `28` -> angka (integer)

### Menampilkan Variabel

```python
nama = "Bengs"
umur = 28

print(nama)
print(umur)
```

```output
Bengs
28
```

### Tipe Data Dasar

| Tipe | Contoh | Penjelasan |
|------|--------|------------|
| `str` | `"Halo"` | Teks |
| `int` | `10` | Bilangan bulat |
| `float` | `3.14` | Desimal |
| `bool` | `True`/`False` | Benar/Salah |

### Cek Tipe Data

```Python
nama = "Bengs"
umur = 28

print(type(nama))
print(type(umur))
```

```Output
<class 'str'>
<class 'int'>
```

### Latihan 1

Buat Variabel:

* `nama` = Nama
* `umur` = Umur
* `tinggi` = tinggi badan (boleh desimal)

Lalu tampilkan semuanya.

### Latihan 2

Tentukan tipe data dari:

```Python
a = "10"
b = 10
c = 10.5
d = True
```

Tuliskan:

* a = ?
* b = ?
* c = ?
* d = ?

### Latihan 3

```Python
x = 5
y = "5"

print(x)
print(y)
```

### Mini Project

Buat program **BIODATA versi variabel**:

```python
nama = ...
umur = ...
hobi = ...

# tampilkan seperti ini:
Nama saya ...
Umur saya ...
Hobi saya ...
```

### Jawaban

**Latihan 1**:

```Python
nama = "Bengs"
umur = 28
tinggi = 172.5

print(nama)
print(umur)
print(tinggi)
```

```Terminal
Bengs
28
172.5
```

**Latihan 2**:

```
a = `str`
b = `int`
c = `float`
d = `bool`
```

**Latihan 3**:

```Terminal
5
5
```

**Mini Project**:

```Python
nama = "Bengs"
umur = 28
hobi = "Coding"

print("Nama saya", nama)
print("Umur saya", umur)
print("Hobi saya", hobi)
```

```Terminal
Nama saya Bengs
Umur saya 28
Hobi saya Coding
```