# Materi 2: Perulangan ("Loops") dan Sekuensial ("Sequences")

## 2.1 Bekerja Dengan Perulangan dan Sekuensial

### Apa itu "List" dan Bagaiaman Cara Kerjanya?

Dalam beberapa materi kedepan kita akan membahas tentang *List*, *Tuple* dan *Range*, dimana merupakan tipe data sekuen di Python.

**List** merupakan sebuah sekuen terurut dari elemen yang bisa terdiri dari *string*, *number*, bahkan *list* didalamnya. *List* merupakan data *mutable* dan menggunakan *index*, diamana index merupakan urutan yang dimulai dari *nol*.

Berikut merupakan contoh sintaks dari *List*:

```python
cities = ['Los Angeles', 'London', 'Tokyo']
```

Untuk mengakses elemen yang ada di dalam *list* `cities`, kita dapat merefernsikannya berdasarkan urutan index di dalam sekuen. Contoh kita akan mengakses elemen pertama dari list tersebut:

```python
cities = ['Los Angeles', 'London', 'Tokyo']
cities[0] # 'Los Angeles'
```

*Negative Indexing* digunakan untuk mengakses elemen dari urutan yang paling belakang, untuk mengaksesnya kita bisa menggunakan `-1` seperti berikut:

```python
cities = ['Los Angeles', 'London', 'Tokyo']
cities[-1]  # Tokyo
```

Cara lain untuk membuat sebuah *list*, kita dapat menggunakan konstruktor `list()`. Kita menggunakannya untuk mengkonversi *iterable* seperti berikut:

```python
developer = 'Jessica'
list(developer) # ['J', 'e', 's', 's', 'i', 'c', 'a']
```

Sebuah *iterable* adalah objek khusus yang dapat dilakukan perulangan berkali-kali.

Untuk mendapatkan panjang dari sebuah list, kita bisa menggunakan fungsi `len()`:

```python
numbers = [1, 2, 3, 4, 5]
len(numbers)  # 5
```

Jika kita perlu melakukan update terhadap sebagian index, kita bisa melakukannya seperti berikut:

```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages)  # ['JavaScript', 'Java', 'C++', 'Rust']
```

List adalah tipe data mutable, kita bisa melakukan update elemen pada list selagi kita dapat memastikan urutan index dengan benar. Jika kita memasukkan urutan index yang tidak sesuai, maka kita akan menerima pesan *error* `IndexError`:

```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[10] = 'JavaScript'

'''
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list assignment index out of range
'''
```

Jika kita ingin menghapus sebuah elemen di dalam sebuah list, kita dapat menggunakan kata kunci `del` untuk melakukannya:

```python
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer)  # ['Jane Doe', 'Python Developer']
```

Terkadang kita perlu mengecek apakah suatu elemen berada di dalam list atau tidak, untuk melakukannya kita dapat menggunakan kata kunci `in` untuk memastikannya:

```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']

'Rust' in programming_languages # True
'JavaScript' in programming_languages # False
```

Terkadang umum ditemukan sebuah list bersarang di dalam list seperti berikut:

```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
```

Dalam contoh tersebut, *nested list* list bersarang menempati index `2` di dalam sebuah list, kita dapat mengaksesnya berdasarkan posisi index nya:

```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2]  # ['Python', 'Rust', 'C++']
```

Kemudian kita bisa mengakses elemen dalam *list bersarang* tersebut sesuai dengan index di dalamnya:

```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2][1] # 'Rust'
```

Teknik umum lain yang biasa digunakan untuk *list* adalah *unpacking list values*.

*Unpacking* pada sebuah list, dimaksudkan untuk menugaskan nilai di dalamnya ke dalam variabel baru. Berikut contoh melakukan *unpacking* terhadap list `developer` dan menugaskan nilai nya ke varibel `name`, `age` dan `job`.

```python
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer

print(name) # 'Alice'
print(age)  # 34
print(job)  # 'Rust Developer'
```

`name` menyimpan nilai `'Alice'`, `age` menyimpan nilai `34`, dan `job` menyimpan nilai `'Rust Developer'`.

Jika kita perlu mengumpulkan sisa elemen dari seubah list, kita dapat menggunakan operator *asterisk* `*`:

```python
developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer

print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']
```

Dalam contoh tersebut, `name` tetap menyimpan nilai `'Alice'`, dan `rest` menyimpan sisa elemen yang belum di masukkan yaitu `34` dan `Rust Developer`.

Jika jumlah varibel yang disiapkan untuk menampung elemen list melebihi jumlah elemen pada list, kita dapat menerima *error* `ValueError`:

```python
developer = ['Alice', 34, 'Rust Developer']
name, age, job, city = developer

'''
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: not enough values to unpack (expected 4, got 3)
'''
```

Konsep terakhir adalah melakukan slicing terhadap list menggunakan operator `:`. Mirip seperti *string slicing* kita bisa mengambil hanya sebagian elemen saja pada suatu list:

```python
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
desserts[1:4] # ['Cookies', 'Ice Cream', 'Pie']
```

Cara lain dalam melakukan slicing adalah dengan menentukan interval untuk melakukan increment elemen yang diakses. Berikut contohnya:

```python
numbers = [1, 2, 3, 4, 5, 6]

numbers[1::2] # [2, 4, 6]
```

### Apa Saja "Method" Umum yang Digunakan untuk List?



### Apa itu "Tuple" dan Bagaimana Cara Kerjanya?

### Apa Saja "Method" Umum yang Digunakan untuk Tuple?

### Bagaimana Cara Kerja "Loops"?

### Apa itu "Range" dan Bagaimana Cara Menggunakannya Dengan Loops?

### Apa itu Fungsi "Enumerate" dan "Zip" dan Bagaimana Cara Kerjanya?

### Apa itu "List Comprehension" dan Apa Fungsi yang Sangat Berguna untuk Digunakan Dengan List?

### Apa itu Fungsi Lambda dan Bagaimana Cara Kerjanya?

## Workshop: Membangun "Pin Extractor"

## Lab: Membangun "Number Pattern Generator"