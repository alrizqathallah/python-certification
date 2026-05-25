# Materi 1: Python Dasar

## 1.1 Pengenalan Python

### Apa itu Python dan Apa Kegunaan Utamanya di Industri?

Python adalah Bahasa Pemrograman yang terkenal dengan sintaks yang simpel dan mudah untuk digunakan. Hal tersebut Python menjadi bahasa pemrograman paling populer di dunia saat ini.

Python digunakan dibanyak bidang, seperti *Data Science* dan *Machine Learning*, *Web Development*, *Scripting* dan *Automation*, *Embedded Systems*, *IoT* dan masih banyak lagi.

Python adalah bahasa utama yang digunakan oleh para *Data Scientist* dan Insinyur *Machine Learning* saat ini. *Library* seperti **Pandas** dan **Numpy** membuat data analisis lebih mudah dilakukan, sementara yang lain seperti **TensorFlow** dan **Scikit** membuat *machine learning* dan bekerja dengan *AI models* lebih gampang diakses.

Dalam pengembangan web, Python memiliki *frameworks* seperti **Django**, **FastAPI** dan **Flask** yang memungkinkan para developer membangun sistem *back-end* lebih *scalable* dan *secure* secara cepat. Banyak platform sosial media menggunakan Python sebagai back-end seperti *Instagram* dan *Pinterest*.

Profesional *Cybersecurity* dan *Ethical Hackers* menggunakan Python untuk mendeteksi kerentanan seperti *Malware* dan *Virus*, membangun sistem keamanan otomatis yang dapat melakukan pembacaan dan analisa ancaman yang datang.

Python berjalan dengan baik di komputer-mikro seperti *Raspberry Pi* dan sirkuit yang kompatibel dengan *Micro-Python*, yang dapat memungkinkan untuk membangun proyek-proyek *IoT*.

Python digunakan secara luas dalam bidang *DevOps* untuk membuat skrip yang dapat digunakan dalam proses *CI/CD* dan mengelola infrastruktur antar jalur pengembangan. Termasuk membangun servis lokal sebagai *Internal API*.

Dalam pengujian perangkat lunak, *tools* berbasis Pyhton seperti **Pytest** digunakan untuk membuat rangkaian tahap pengujian, termasuk melakukan sistem monitoring dan manajeman *log*.

Akhirnya, satu dari yang paling besar penggunaan Python di industri adalah dalam bidang *Automation*. Kita dapat menulis skrip simpel yang memungkinkan kita bisa melakukan tugas rutin seperti melakukan ekstraksi data dari spreadsheet, mengirim email dan bekerja dengan file lebih efisien dan otomatis.

Pustakan seperti **Selenium** dan **BeautifulSoup** juga dapat melakukan interkasi dengan palatform web, sehingga kita dapat melakukan *scrapping* data publik, mengotomatisasi interaksi dengan UI sampai mengelola *Cloud Project* dengan otomatis

Seperti yang sudah diketahui sebelumnya, Python merupakan bahasa pemrograman yang *powerful*, tidak hanya itu, Python juga mudah untuk dipelajari.

Python adalah pilihan yang tepat untuk siapa pun yang memulai untuk belajar pemrograman, terlepas apa pun bidang yang akan dipilih selanjutnya.

### Bagaimana Cara Menginstal, Mengkonfigurasikan dan Menggunakan Python di Komputer Lokal?

Cara termudah untuk melaukan instalasi Python di *Windows* dan *Mac* adalah dengan mendownload *installer* dari sumber (web) resmi Python. Kita juga akan mempelajari cara menjalankan Python di *Linux*.

Silakan kunjungi [python.org](https://python.org/downloads) dan silakan download installer Python sesuai dengan sistem operasi yang digunakan. Secara umum web resmi Python akan mendeteksi sistem operasi yang digunakan secara otomatis.

Melakukan instalasi di macOS:

* Pilih dan klik download installer, yang secara otomatis akan mendownload file installer berbentuk `.pkg`.

* Setelah terdownload, buka dan klik "continue" di dalam jendela tampilan yang muncul.

* Klik "continue" sampai menemukan bagian "Installation Type". Setelah itu klik tombol "Install".

* Masukan password yang diminta, dan tunggu sampai instalasi selesai.

* Setelah proses instalasi selesai, kita akan mendapatkan pesan selamat telah menginstal Python.

* Tekan "Close" dan selesai.

Kemudian silakan buka terminal dan ketik `python --version` atau `python3 --version`.

Perlu dicatat, terkadang sistem akan terjadi bentrokan antar perintah yang sering muncul di sistem macOS dan Linux. Jika di sistem tersebut terdapat atau sudah terpasang Python versi lama, seperti *Python 2*, ketika mencoba menjalankan program dengan perintah `python --version` akan terjadi kebingungan karena ada dua atau lebih versi Python yang terpasang, untuk mengatasinya gunakna perintah yang spesifik seperti `python3` atau `python2` diawal, dan tidak disarankan menggunakan `python` jika ada lebih dari satu versi Python yang terpasang di komputer lokal. Hal itu juga berlaku ketika kita menjalankan program python dengan interpreter yang sesuai dengan versi Python yang terpasang.

Instalasi Python di Windows:

* Silakan kunjungin website resmi Python dan download file installer yang dibutuhkan. Pastikan mendownload installer Python versi/khusus Windows.

* Secara otomatis akan mengunduh file installer dalam bentuk `.exe`.

* Setelah file installer terunduh, silakan klik file tersebut dan ikuti langkah instalasi seperti proses instalasi pada umumnya.

* Ketika mencapai/menemui bagian penambahan PATH di jendela layar, pastikan kita mencentang kolom `Add Python .exe to PATH`. Hal tersebut akan memudahkan kita, sehingga tidak perlu menambahkan file eksekusi ke PATH secara otomatis di Windows.

Setelahnya lakukan verifikasi, dengan mengetikan perintah `python --version`, jika proses intalasi dan konfigurasi benar, maka akan ditampilkan versi Python yang terpasang.

Secara umum Python sudah tersedia di banyak distro besar Linux, macam Ubuntu, Debian dan Fedora.

Kita cukup melakukan verifikasi saja, terhadap versi Python yang digunakan di distro Linux tersebut.

Selengkapnya silakan kunjungi website resmi Python [python.org](https://python.org/downloads) dan cari langkah instalasi sesuai dengan sistem operasi yang digunakan.

---

## 1.2 Variabel dan Tipe Data

### Bagaimana Cara Mendeklarasikan Variabel dan Apa itu Konvensi Penamaan untuk Variabel?

Di Python, *variabel* seperti sebuah wadah yang memiliki label yang digunakan untuk menyimpan data dan mereferensikan tipe datanya. Untuk mendeklarasikan varibel di Python, kita cukup melakukan *assignment* menggunakan operator `=` terhadap variabel, tanpa menggunakan kata kunci khusus seperti `let` atau `const` yang umum digunakan di bahasa pemrograman lain.

Dalam Python, kita cukup menulis nama variabel di sebelah kiri, diikuti operator penugasan, dan *value* di sebelah kanan. Seperti contoh berikut:

```python
name = 'John Doe'
age = 25
```

Dalam contoh tersebut variabel `name` memiliki value `'John Doe'`. Value tersebut adalah string, merupakan kumpulan karakter yang digunakan untuk merepresentasikan teks. *String* ditulis dengan tanda kurung satu `' '` atau bisa juga dengan tanda kurung dua `" "`.

Ketika memberi nama variabel di Python, kita perlu cermat mengenai aturan penulisan berikut:

* Nama varibel hanya dapat dimulai dengan huruf (*alfabetikal*) dan simbol `_` (*underscore*), bukan bilangan (*numerik*).

* Nama varibel dapat mengandung karakter *alfanumerik* (`a-z`, `A-Z`, `0-9` dan `_`).

* Nama varibel bersifat *case-sensitive*, yang berarti semua nama harus bersifat unik, antar `age`, `Age` dan `AGE` dianggap berbeda, meski secara harfiah dianggap sama, dikarenakan format tulisan yang berbeda.

* Kita tidak bisa menggunakan *reserve keywords* (kata kunci khusus) yang telah ditetapkan oleh Python, seperti `if`, `class` atau `def`.

Jika kita melanggar aturan penulisan tersebut, maka Python akan mengembalikan pesan *Error* (`SyntaxError`):

```terminal
    5variable_name = 5
     ^
SyntaxError: invalid syntax
```

Sekarang, mari kita masuk kedalam konvensi penamaan variabel di Python.

Pertama, variabel harus bersifat deskriptif, dan menggunakan huruf *lowercase* (huruf kecil) dipisahkan dengan *underscore* (`_`), yang biasa dikenal dengan istilah format **camel-case**.

Contoh:

```python
my_varible_name = 'freeCodeCamp'
```

Selanjutnya, kita harus membuat nama varibel bersifat deskriptif, sebagai contoh, jika kita memerlukan informasi usia dari pengguna, lebih baik kita menggunakan anam `user_age`, dari pada hanya `age`, terlebih `ua` yang hanya sebuah singkatan.

```python
user_age = 30
```

Dengan model penamaan tersebut, kita dapat mengkomunikasikan kebutuhan variabel kepada rekan di tim/orang lain.

Sangat disarankan untuk menghindari penamaan variabel dengan *single-letter*, karena model penamaan tersebut tidak memberikan arti apa pun.

```python
x = 56  # Apa maksdunya x?
```

Sebuah simbol *pawn* (`#`) yang diikuti dengan teks, disebut denga komentar (*comments*). 

Di Python, komentar diawali dengan `#`, dan akan mengabaikan apa pun yang ditulis setelahnya pada baris tersebut.

```python
# This is a single-line comment
```

Kita dapat membuat komentar menjadi multi baris, dengan membuatnya secara berturut.

```python
# This is
# multi-line
# comment
```

Kita dapat menggunakan komentar untuk memberikan penjelasan terhadap kode, meninggalkan pesan khusus untuk orang lain/menjelaskan detail terhadap baris tertentu. Hal ini saya penting ketikan bekerja dalam sebuah tim.

Bagaimana pun, kita tidak perlu menggunaka komentar untuk menjelaskan penamaan variabel. Karena penamaan variabel seharusnya memiliki arti dan bersifat deskriptif.

### Bagaimana fungsi `print()` bekerja?

Di setiap bahasa pemrograman memiliki cara atau fungsi bawaan yang digunakan untuk menampilkan pesan ke layar terminal. Python menggunakan fungsi `print()` untuk menampilkan data ke terminal.

```python
print('Hello world!') # Hello world!
```

`'Hello world!'` di dalam fungsi `print` merupakan sebuah string. String tersebut dimasukan sebagai **argument** di dalam fungsi `print`, kita juga dapat menggunakan **multiple argumen** untuk menampilkan data secara bersamaan.

```python
print('My favorite colors are', 'blue', 'green', 'red')
# Output: My favorite  colors are blue green red
```

Python secara otomatis memisahkan, atau memberi jarak satu spasi terhadap argumen yang dipisah oleh tanda koma tersebut. Hal tersebut sangat membantu ketika kita perlu mencetak beberapa informasi secara bersamaan.

### Apa Saja Tipe Data di Python dan Bagaimana Cara Mengetahui Tipe Data dari Sebuah Variabel?

Sebelum bekerja dengan varibel di Python, penting untuk mengetahui apa itu *Data Types* (Tipe Data) terlebih dahulu. Sebuah tipe data akan mendeskripsikan jenis dari sebuah data yang disimpan oleh varibel. Sebagai contoh, *number*, *teks* atau *list* dari kumpulan item. 

Python merupakan *dyanamically typed language*, yang berarti kita tidak perlu secara eksplisit menentukan tipe data untuk sebuah variabel. Program akan secara otomatis mengetahui tipe data apa yang disimpan oleh varibel, setelah value disamukkan.

```python
name = 'John Doe'       # Python mengethaui ini sebagai sebuah STRING
age = 25        # Python mengetahui ini sebagai sebuah INTEGER
```

Hal tersebut sangat kontras dengan Bahasa Pemrograman lain seperti C#, Java dan C++, dimana kita perlu mendeklarasikan variabel dengan tipe data tertentu secara eksplisit.

```
string name = 'John Doe'
int age = 25
```

Karena bahasanya yang dinamis, membuat Python sangat cepat dalam penulisan dan fleksibel. Tetapi hal tersebut juga dapat menyebabkan *typed error* ketikan program dijalankan.

Python mengeksekusi program dari atas kebawah, baris per baris. Ketikan Python membaca kode program menemui kesalahn atau *error* dibaris yang ditemui, maka secara langsung program akan berhenti di baris tersebut, dan mengembalikan pesan error.

Hal tersebut juga menjadi perilakuk yang kontras dimana, dalam bahasa pemrograman lain, program dapat ditemui kesalahannya atau error ketika kode program di kompilasi. Sehingga bisa di perbaiki sebelum kode tersebut dijalankan.

Dengan demikian, mungkin kita tidak dapat mengetahui kesalahan secara pasti sampai kode program benar-benar di jalankan.

Berikut merupakan beberapa tipe data yang umum digunakan di Python:

* Integer: Merupakan tipe data bilangan bulat (`10` atau `-5`).
  ```python
  my_integer_var = 10
  print('Integer:', my_integer_var) # Integer: 10
  ```

* Float: Merupakan bilangan pecahan/koma seperti `4.41` atau `-0.4`.
  ```python
  my_float_var = 4.50
  print('Float:', my_float_var) # Float: 4.5
  ```

* String: Merupakan rangkaian karakter yang membentuk teks, diapit dengan tanda kutip satu atau dua `Hello world!`.
  ```python
  my_string_var = 'hello'
  print('String:', my_string_var) # String: hello
  ```

* Boolean: Merupakan data yang merepresentasikan benar dan salah (`True` dan `False`).
  ```python
  my_boolean_var = True
  print('Boolean:', my_boolean_var) # Boolean: True
  ```

* Set: Merupakan tipe data kumpulan elemen unik tidak berurut, seperti `{0.5, 4, 'apple'}`.
  ```python
  my_set_var = {7, 'hello', 8.5}
  print('Set:', my_set_var) # Set: {7, 'hello', 8.5}
  ```

* Dictionary: Merupakan tipe data yang berisikan koleksi pasangan kunci dan nilai (*key-value pairs*), `{'name': 'John Doe', 'age': 28}`.
  ```python
  my_dictionary_var = {'name': 'Alice', 'age': 25}
  print('Dictionary:', my_dictionary_var) # Dictionary: {'name': 'Alice', 'age': 25}
  ```
* Tuple: Merupakan koleksi datat terurut yang *immutable*, di simpan dalam tanda kurung `( )`, `('apple', 4.5, 7)`
    ```python
    my_tuple_var = (7, 'hello', 8.5)
    print('Tuple:', my_tuple_var) # Tuple: (7, 'hello', 8.5)
    ```

* Range: Merupakan rangkaian bilangan, biasa digunakan untuk perulangan, `range(5)`.
    ```python
    my_range_var = range(5)
    print('Range:', my_range_var)   # Range: range(0, 5)
    ```

* List: Merupakan urutan koleksi elemen terurut yang mendukung perbedaan tipe data.
    ```python
    my_list = [22, 'Hello world', 3.14, True]
    print(my_list) # [22, 'Hello world', 3.14, True]
    ```

* None: Merupakan tipe data khusus yang merepresentasikan kekosongan data/value.
    ```python
    my_none_var = None
    print('None:', my_none_var) # None: None
    ```

Untuk dapat mengetahui tipe data dari sebuah variabel, kita dapat menggunakan fungsi `type()`.

```python
my_var_1 = 'Hello world'
my_var_2 = 21

print(type(my_var_1)) # <class 'str'>
print(type(my_var_2)) # <class 'int'>
```

Berikut merupakan konvensi fungsi `type()` untuk semua tipe data di Python:

```python
my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 'hello', 8.5}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 'hello', 8.5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list)) # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>
```

Fungsi bawaan `isinstance()` memungkinkan kita melakukan *matching* terhadap value dan tipe data. Fungsi ini akan mengembalikan pesan boolean. Jika nilai cocok dengan tipe data, maka akan mengembalikan nilai `True`, tetapi jika tidak cocok akan mengembalikan nilai `False`.

```python
isinstance('Hello world', str) # True
isinstance(True, bool) # True
isinstance(42, int) # True
isinstance('John Doe', int) # False
```

## Workshop: Membangun "Report Card Printer"

```python
name = 'Alice'
print(name, type(name))

is_student = True
print(is_student, type(is_student))

age = 20
print(age, type(age))

score = 80.5
print(isinstance(score, float))
print(score, type(score))
```

```terminal
Alice <class 'str'>
True <class 'bool'>
20 <class 'int'>
True
80.5 <class 'float'>
```

---

## 1.3 Pengenalan String

### Apa itu String dan Apa itu String Immutabilitas?

**String** adalah rangkaian karakter yang dibungkus dengan tanda kutip satu `' '` atau tanda kutip dua `" "`. Dalam beberapa bahasa pemrograman, terdapat perbedaan perilaku antara string yang menggunakan kutip satu `' '` dengan string yang menggunakan kutip dua `" "`. Di Python, keduanya di perlakukan dengan sama. Jadi kita bisa menggunakan keduanya.

```python
my_str_1 = 'Hello'
my_str_2 = "World"
```

Kita juga bisa menggunakan *multi-line string* di Python.

```python
my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''
```

Jika di dalam string kita membutuhkan karakter kutip, kita bisa menggunakan kutip yang berlawanan.

```python
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'
```

Atau, kita bisa menggunakan karakter sequence. Karakter sequence ditandai dengan *backslash* `\`, yang diikuti dengan karakter sequence yang diinginkan.

```python
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
```

Terkadang kita perlu melakukan pemeriksaan terhadap string yang menyimpan satu atau lebih karakter. Untuk itu Python menyediakan operator `in` yang akan mengembalikan pesan boolean, jika suatu teks/karakter ada di dalam sebuah rangkaian string.

```python
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False
```

Sekarang, mari kita cari tahu bagaimana cara mengetahui panjang sebuah string dan bekerja dengan single karakter di dalam string tersebut. Proses ini dikenal dengan istilah **Indexing**. Untuk melakukannya kita bisa menggunakan fungsi bawaah `len()`.

```python
my_str = 'Hello world'
print(len(my_str))  # 11
```

Masing-masing karkater pada rangkaian string menempati posisi yang disebut sebagai *index*. Hitungan **Index** dimulai dari bilangan `0`, yang merupakan bilangan pertama dari sebuah index. Sementari bilangan/urutan kedua dari sebuah index adalah bilangan `1`, dan seterusnya. Untuk mengakses kerakter string di dalam index, kita dapat menggunakan `[ ]`.

```python
my_str = "Hello world"

print(my_str[0])    # H
print(my_str[6])    # w
```

**Negagtive Indexing** memungkinkan kita untuk mendapatkan karakter terakhir dalam sebuah string dengan `-1`, dan karakter terakhir kedua dalam sebuah string dengan `-2`.

```python
my_str = 'Hello world'
print(my_str[-1])  # d
print(my_str[-2]) # l
```

Banyak bahasa pemrograman yang membedakan antara data *primitif* dan *reference*. Maksud dari tipe primitif adalah dimana data tersebut merupakan *immutable*, yang berarti tidak dapat diganti setelah dideklarasikan. Sementara reference menyimpan data yang bersifat koleksi/banyak, sebagian ada yang *immutable* dan *mutable*. Tetapi Python tidak memberikan garis besar antara keduanya. Alih-alih menggunakan cara yang sama, tipe data di Python diperlakukan sebagai *object*, sebagian objek bersifat *immutable* dan sebagian yang lain *mutable*.

Tipe data *immutable* tidak dapat dimodifikasi setelah value tersebut dimasukkan. Kita hanya bisa menggantinya dengan value yang berbeda, atau biasa disebut dengan *reassignment*.

String adalah tipe data immutable. Artinya kita dapat melakukan *reassignment* dengan value string baru/berbeda.

```python
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello
```

Contoh lain tipe data yang immutable di Python adalah `integer`, `float`, `boolean`, `tuple` dan `range`.

### Apa itu String Konkatenasi dan String Interpolasi?

Ketika kita bekerja dengan string, mengkombinasikan string secara bersamaan merupakan hal yang umum akan dilakukan.

Di Python, menggabungkan string dapat dilakukan dengan menggunakan operator `+`. Proses tersebut dikenal dengan istilah **String Concatenation**.

```python
my_str_1 = 'Hello'
my_str_2 = 'World'

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World
```

Perlu dicatat, jika kita memaksa untuk melakukan konkatenasi string dengan bilangan, maka akan terjadi `TypeError`.

```python
name = 'John Doe'
age = 26

name_and_age = name + age
print(name_and_age) # TypeError: can only concatenate str (not "int") to str
```

Hal tersebut terjadi karena string tidak secara otomatis mengkonversi tipe data ke dalam tipe data lain yang seharusnya. Untuk memperbaiki hal tersebut, kita dapat melakukan **casting** bilangan kedalam bentuk string dengan fungsi `str()`.

```python
name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26
```

Kita juga dapat melakukan konkatenasi string menggunakna operator *augmented assignment* seperti `+=`.

```python
name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26
```

Proses memasukkan varibel dan ekspresi kedalam sebuah string disebut dengan **string interpolation**. Python memiliki kategori yang disebut **f-string** yang dapat digunakan untuk melakukannya.

F-string dimulai dengan menambahkan huruf `f` di depan tanda kutip string. Kita dapat memanggil varibel didalam string menggunakan tanda kurung kurawal `{ }`.

```python
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15
```

### Apa itu String "Slicing" dan Bagaiaman Cara Kerjanya?

Dalam materi sebelumnya, bagaimana setiap karakter string dapat diidentifikasi posisi index nya dan di akses menggunakan `[ ]`.

```python
my_str = "Hello world"

print(my_str[0]) # H
print(my_str[6]) # w
print(my_str[-1]) # d
```

**String slicing** memungkinkan kita untuk mengekstrak bagian string secara spesifik atau sebagian string.

```
string[start:stop]
```

Jika kita ingin mengekstrak dari index tertentu ke index tertentu, kita cukup memisahkan index `start` dan index `stop` dengan simbol titik dua `:`.

```python
my_str = 'Hello world'
print(my_str[1:4])  # ell
```

Perlu dicatat, bahwa `stop` index adalah non-inklusif, jadi `[1:4]` itu hanya mengekstrak karakter dari index `1` dan seterusnya, tidak termasuk karakter di index `4`.

Kita bisa menetapkan `start` dan `stop` secara default, yaitu `0` dan awal atau akhir yang ditentukan.

```python
my_str = 'Hello world'
print(my_str[:7])   # Hello w
```

```python
my_str = 'Hello world'
print(my_str[8:])  # rld
```

Selain parameter `start` dan `stop`, ada juga langkah opsional `step` parameter yang digunakan untuk mengindikasikan increment di antara index.

```
string[start:stop:step]
```

```python
my_str = 'Hello world'
print(my_str[0:11:2])   # Hlowrd
```

Salah satu trik yang sangat membantu untuk melakukan reverse pada string adalah dengan memberikan nilai `-1` pada parameter `step` dan masing-masing `0` untuk `start` dan `stop`.

```python
my_str = 'Hello world'
print(my_str[::-1])     # dlrow olleH
```

### Apa Saja "Method" String yang Umum Digunakan di Python?

Python menyediakan beberapa *method* bawaan yang dapat digunakan untuk memanipulasi string.

* `upper()`: Akan merubah string dengan huruf besar secara keseluruhan.
```python
my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD
```

* `lower()`: Akan merubah string menjadi huruf kecil secara keseluruhan.
```python
my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world
```

* `strip()`: Akan akan membersihkan *whitespace* atau spasi di awal dan akhir string.
```python
my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"
```

* `replace(old, new)`: Akan mengganti rangkaian string secara spesifik dengan nilai lain.
```python
my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world
```

* `split(separator)`: Memisahkan sebuah string berdasarkan pemisah yang ditentukan menjadi daftar string. Jika tidak ada pemisah yang ditentukan, maka akan dipisahkan berdasarkan spasi.
```python
my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']
```

* `join(iterable)`: Menggabungkan elemen-elemen dari sebuah iterable menjadi sebuah string dengan pemisah.
```python
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)    # hello world
```

* `startswith(prefix)`: Mengembalikan nilai boolean yang menunjukkan apakah sebuah string diawali dengan awalan yang ditentukan.
```python
my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True
```

* `endswith(suffix)`: Mengembalikan nilai boolean yang menunjukkan apakah sebuah string diakhiri dengan akhiran yang ditentukan.
```python
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True
```

* `find(substring)`: Mengembalikan indeks kemunculan pertama substring, atau `-1` jika tidak ditemukan.
```python
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)  # 6
```

* `count(substring)`: Mengembalikan jumlah berapa kali sebuah substring muncul dalam sebuah string.
```python
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)  # 2
```

* `capitalize()`: Mengembalikan string baru dengan karakter pertama berupa huruf kapital dan karakter lainnya berupa huruf kecil.
```python
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world
```

* `isupper()`: Mengembalikan nilai `True` jika semua huruf dalam string adalah huruf besar dan `False` jika tidak.
```python
my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False
```

* `islower()`: Mengembalikan nilai `True` jika semua huruf dalam string adalah huruf kecil dan `False` jika tidak.
```python
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True
```

* `title()`: Mengembalikan string baru dengan huruf pertama setiap kata dikapitalisasi.
```python
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World
```

## Workshop: Membangun "Employee Profile Generator"

```python
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)
year_code = employee_code[4:8]
initials = employee_code[9:11]
print(year_code)
print(initials)
last_three = employee_code[-3:]
print(last_three)
```

```terminal
Experience: 5 years
Employee: John Doe | Age: 28 | Position: Data Analyst | Salary: $75000
DEV
2026
JD
001
```
## 1.4 Bilangan dan Operasi Matematika

### Bagaimana Cara Kerja Bilanagan ("Integer") dan Desimal ("Floating Point")?

**Integers** dan **Floats** adalah tipe data numerik utama di Python. Dengan tipe data tersebut kita bisa menyimpan data numerik dan melakukan operasi matematika.

*Integer* adalah bilangan bulat tanpa kome (*desimal points*), baik positif dan negatif:

```python
my_int_1 = 56
my_int_2 = -4

print(type(my_int_1))   # <class 'int'>
print(type(my_int_2))   # <class 'int'>
```

Penjumlahan dengan menggunakan integer:

```python
my_int_1 = 56
my_int_2 = 12

sum_ints = my_int_1 + my_int_2
print('Integer Addition:', sum_ints)    # Integer Addition: 68
```

Pengurangan dengan menggunakan integers:

```python
my_int_1 = 56
my_int_2 = 12

diff_ints = my_int_1 - my_int_2
print('Integer Subtraction:', diff_ints)    # Integer Subtraction: 44
```

Perkalian dengan menggunakan integers:

```python
my_int_1 = 12
my_int_2 = 4

product_ints = my_int_1 * my_int_2
print('Integer Multiplication:', product_ints)  # Integer Multiplication: 48
```

Pembagian dengan menggunakan integers:

```python
my_int_1 = 56
my_int_2 = 12

div_ints = my_int_1 / my_int_2
print('Division:', div_ints)    # Division: 4.666666666666667
```

*Floats* adalah bilangan positif atau negatif dalam bentuk pecahan (*decimal points*).

```python
my_float_1 = -12.0
my_float_2 = 4.9

print(type(my_float_1)) # <class 'float'>
print(type(my_float_2)) # <class 'float'>
```

Berikut penjumlahan dengan menggunakan floats:

```python
my_float_1 = 5.4
my_float_2 = 12.0

float_addition = my_float_1 + my_float_2
print('Float Addition:', float_addition)    # Float Addition: 17.4
```

Berikut pengurangan dengan menggunakan floats:

```python
my_float_1 = 5.4
my_float_2 = 12.0

float_subtraction = my_float_2 - my_float_1
print('Float Subtraction:', float_subtraction)  # Float Subtraction: 6.6
```

Berikut perkalian dengan menggunakan floats:

```python
my_float_1 = 5.4
my_float_2 = 12.0

float_multiplication = my_float_2 * my_float_1
print('Float Multiplication:', float_multiplication)
```

Dan berikut pembagian dengan floats:

```python
my_float_1 = 5.4
my_float_2 = 12.0

float_division = my_float_2 / my_float_1
print('Float Division:', float_division)
```

Jika kita menambahkan integer dengan float, maka hasil secara otomatis dikonversi ke dalam bentuk float:

```python
my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float)    # 61.4
print(type(sum_int_and_float))  # <class 'float'>
```

Hal tersebut berlaku untuk banyak operasi matematikan lain seperti pengurangan, perkalian dan pembagian. Jika kita campur integer dan float, Python akan mengembalikan hasil dalam bentuk float.

Kita juga bisa melakukan operasi matematika kompleks seperti *modulo*, *floor division*, dan *exponention*, dengan kedua *integers* dan *floats*.

Berikut operator `%`:

```python
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print('Integer Modulo:', mod_ints) # Integer Modulo: 8
print('Float Modulo:', mod_floats) # Float Modulo: 1.1999999999999993
```

Berikut untuk operasi *floor division* `//`:

```python
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats) # Float Floor Division: 2.0
```

Berikut merupakan operasi *exponentiation*:

```python
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation:', exp_ints) # Integer Exponentiation: 951166013805414055936
print('Float Exponentiation:',  exp_floats) # Float Exponentiation: 614787626.1765089
```

Terkadang, kita mungkin menyadari bahwa hasil dari operasi yang menghasilkan bilangan float memiliki desimal yang banyak. Sebagai contoh, penjumlahan `0.1 + 0.2` sama dengan `0.30000000000000004`, ketimbang `0.3`.

Hal tersebut terjadi dikarenakan bilangan di simpan dalam format biner, dan sebagian pecahan tidak dapat direpresentasikan secara tepat dalam biner. Akibatnya, angka-angka tersebut disimpan sebagai perkiraan terbatas, sama seperti pecahan `1/3` yang tidak dapat direpresentasikan dengan jumlah digit terbatas dalam desimal dan dipotong setelah sejumlah digit tak terbatas (`0,33333...`).

Hal tersebut menyebabkan kesalahan pembulatan kecil.

Python juga menyediakan fungsi bawaan untuk mengkonveriskan data numerik atau string kedalam bentuk float.

`float()` merupakan fungsi yang digunakan untuk mengkonversi bilangan kedalam bentuk floats.

```python
my_int_1 = 56
my_float_1 = float(my_int_1)

print(my_float_1)   # 56.0
print(type(my_float_1)) # <class 'float'>
```

Begitupun denga operator konversi `int()`:

```python
my_float = 12.92563
my_int = int(my_float)

print(my_int)   # 12
print(type(my_int)) # <class 'int'>
```

Kita juga bisa menggunakan fungsi bawaan untuk mengkonversi sebuah string baik float dan integer:

```python
my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))   # 45 <class 'int'>
print(converted_float, type(converted_float))   # 7.8 <class 'float'>
```

Berikut merupakan beberapa method yang dapat digunakan untuk bekerja denga *integer* dan *float*.

* `round()`: Digunakan untuk membulatkan bilangan desimal. Secara default, fungsi ini membulatkan ke bilangan bulat terdekat, dan mengembalikan bilangan bulat tanpa desimal:
```python
my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1) # 5
print(rounded_int_2)    # 4.3
```

* `abs()`: Mengembalikan nilai absolut dari sebuah bilangan
```python
num = -15

absolute_value = abs(num)
print(absolute_value)   # 15
```

* `pow()`: Digunakan untuk memangkatkan bilangan dengan bilangan lain atau melakukan eksponensiasi modular.
```python
result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3
```

### Bagaimana Cara Kerja "Augmented Assigment"?

**Augmented Assigment** mengkombinasikan operasi biner dengan sebuah penugasan dalam satu langkah.

Berikut merupakan sintaks *augmented assignment*:

```
variable <operator>= value
```

Cara tersebut lebih efisien dari pada:

```
varible = variable <operator> value
```

Sebagai contoh, berikut penggunaan *augmented assigment* untuk menambahkan `5` pada variabel yang tersedia:

```python
my_var = 10
my_var += 5

print(my_var)   # 15
```

Berikut merupakan hal yang sama tanpa menggunakan *augmented assignment*:

```python
my_var = 10
my_var = my_var + 5

print(my_var)   # 15
```

Kelebihan *augmented assignment* adalah cara simpel untuk melakuka penambahan atau pengurangan nilai pada variabel tanpa perlu mengulang nama varibel tersebut. Hal tersebut dapat mengurangi *redudansi* dan kesalahan tulis yang dapat muncul.

Setiap oprator dapat menggunakan *augmented assignment*:

```python
count = 14
count -= 3

print(count)    # 11

product = 65
product *= 7

print(product)  # 455

price = 100
price /= 4

print(price)    # 25.0

total_pages = 23
total_pages //= 5

print(total_pages)  # 4

bits = 35
bits %= 2

print(bits) # 1

power = 2
power **= 3

print(power)    # 8

greet = 'Hello'
greet += ' World'

print(greet)    # Hello World

greet = 'Hello'
greet *= 3

print(greet)    # HelloHelloHello

# TypeError
greet = 'Hello'
greet -= ' World'

print(greet) # TypeError: unsupported operand type(s) for -=: 'str' and 'str'


greet = 'Hello'
greet /= 'World'

print(greet) # TypeError: unsupported operand type(s) for /=: 'str' and 'str' 
```

Kenapa Python tidak menggunakan operator `++` atau `--`, hal tersebut Python hindari menggunakan pintasan penambahan dan pengurangan ala *c-style* agar tetap jelas dan eksplisit.

## Workshop: Membangun "Bill Splitter"

```python
running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks

print(f'Total bill so far: {running_total}')

tip = running_total * 0.25

print(f'Tip amount: {tip}')

running_total += tip

print(f'Total with tip: {running_total}')

final_bill = running_total / num_of_friends

print(f'Bill per person: {final_bill}')

each_pays = round(final_bill, 2)

print(f'Each person pays: {each_pays}')
```

```terminal
Total bill so far: 198.82999999999998
Tip amount: 49.707499999999996
Total with tip: 248.53749999999997
Bill per person: 62.13437499999999
Each person pays: 62.13
```

## 1.5 Boolean dan Pengkondisian

### Bagaimana Cara Kerja Pengkondisian dan Operator Logika?

*Conditional Statements* atau pengkondisian, memungkinkan kita untuk mengontrol alur kerja program berdasarkan kondisi-kondisi yang mungkin terjadi, `True` atau `False`.

Pada materi sebelumnya, kita telah mengetahui bahwa Python memiliki tipe data *boolean* yang hanya menerima nilai `True` dan `False`.

Berikut merupakan operator komparasi di Python:

* `==`: digunakan untuk mengecek apakah dua nilai memiliki value yang sama.
* `!=`: digunakan untuk mengecek apakah dua nilai tidak memiliki value yang sama.
* `>`: Lebih besar
* `<`: Lebih kecil
* `>=`: Lebih besar dan Sama dengan
* `<=`: Lebih kecil dan sama dengan

```python
print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True
```

Operator tersebut digunakan untuk membandingkan nilai berdasarkan kondisi yang ada dan akan menghasilkan nilai `True` atau `False`.

Python memiliki pengkondisian dasar menggunakan `if`:

```
if condition:
    pass # Code to execute if condition is True
```

* `if` di mulai dengan kata kunci `if`.
* `condition` adalah ekspresi yang melakukan evaluasi yang menghasilkan nilai `True` atau `False`, kemudia diikuti titik dua `:`.
* Bagian isi dari pernyataan `if` membentuk sebuah blok kode, yaitu sekelompok pernyataan yang saling berkaitan. Dalam Python, tingkat indentasi adalah yang mendefinisikan sebuah blok kode.

Dalam contoh diatas, memiliki statement `pass`. Ketika kita memasukkannya maka tidak akan terjadi apapun. `pass` adalah kata kunci khusus yang dapat digunakan sebagai placeholder, atau penampung sementara.

Kode pada blok `if` hanya akan berjalan ketika kondisi yang dievalusasi menghasilkan nilai `True`.

```python
age = 18

if age >= 18:
    print('You are an adult')   # You are an adult
```

Perhatikan indentasi sebelum `print('You are an adult')`. Jika bahasa pemrograman lain menggunakan kurung kurawal untuk mendefinisikan blok kode, Python menggunakan *indentation* sebagai blok kode.

Baris kode berikut akan menampilkan `IndentationError`, dimana hal tersebut mengindikasikan bahwa kode membutuhkan indentasi, sebagian format penulisan kode di Python wajib menggunaakn indentasi.

```python
age = 18

if age > 18:
  print('You are an adult') # IndentationError: expected an indented block after `if` statement on line 3
```

Kita sejatinya dapat menggunakan berapapun jarak indentasi, selagi hal tersebut mendifinisikan indentasi yang dibutuhkan, tetapi Python memiliki rekomendasi indentasi dengan jarak 4 spasi.

Blok kode juga akan ditemukan pada perulangan dan fungsi.

```python
age = 12

if age >= 18:
  print('You are an adult')
```

Dalam kode tersebut, kita mengetahui bahwa `age` kurang dari `18`. Di situasi tersebut kita dapat menggunakan `else`. Pernyataan `else` akan dieksekusi jika pernyataan `if` bernilai `False` setelah dilakukan evaluasi. Pernyataan ini sering dikenal juga dengan blok `if...else`.

```
if condition:
  pass # Dieksekusi jika evaluasi `if` bernilai `True`
else:
  pass # Dieksekusi jika eveluasi `if` bernilai `False`
```

Sebagai contoh:

```python
age = 12

if age >= 18:
  print('You are an adult')
else:
  print('You are not an adult yet')
```

Dalam kasus lain, sangat mungkin kita menemui kondisi yang memerlukan lebih dari 2 hasil kondisi (alternatif). Dalam situasi tersebut kita dapat menggunakan pernyataan `elif` sebagai alternatif dari `if`.

```
if condition1:
  pass
elif condition2:
  pass
else:
  pass
```

Sebagai contoh:

```python
age = 12

if age >= 18:
  print('You are an adult')
elif age >= 13:
  print('You are an teenager')
else:
  print('You are an child')
```

Kita dapat membuat opsi `elif` sebanyak mungkin:

```python
age = 2

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant')
```

### Apa itu Nilai "Truthy" dan "Falsy", Bagaimaan Boolean Operator dan "Short-Circuiting" Bekerja?

Dalam materi sebelumnya, kita telah mempelajari bagaimana menggunakan operator perbandingan dan pernyataan kondisional untuk mengendalikan alur dari suatu program.

Sangat mungkin bagi kita berjalan di sutuasi dimana kita perlu membandingkan beberapa nilai dalam satu kali. Hal tersebut akan memaksa kita melakukan *nested conditional*, pengkondisian beranak.

```python
is_citizen = True
age = 25

if is_citizen:
  if age >= 18:
    print('You are eligible to vote')
else:
  print('You are not eligible to vote')
```

Dalam kode di atas, pertama kita memeriksa jika `is_citizen` adalah `True`, kita akan lanjut ke pernyataan `if` di dalamnya (selanjutnya) yang melakukan pengecekan `age` apakah lebih dari atau sama dengan `18`. Pesan akan dicetak jika pernyataan `if` beranak menghasilkan nilai `True`, jika tidak maka secara otomatis akan mengeksekusi pernyataan `else`, dan mencetak pesan yang ada di dalamnya.

Jika kita bekerja dengan pengkondisian yang kompleks, kita bisa menggunakan operator `and`, `or` dan `not` di Python.

Sebelum lebih jauh mengetahuinya, kita perlu mengerti terlebih dahulu apa itu nilai `Truthy` dan `Falsy`.

Di Python, setiap nilai sejatinya mewakili sifat boolean, secara bawaan diperlakukan seperti `True` atau `False` dalam konteks logika. Sebagian besar nilai ditangkap sebagai nilai `Truthy` yang akan menghasilkan nilai `True`. Sementara sebagian lain di tetapkan sebagai `Falsy` yang akan menghasilkan nilai `False`.

Berikut merupakan beberapa nilai yang dianggap *falsy*:

* `None`
* `False`
* Integer `0`
* Float `0.0`
* Empty String `""`

Lainnya seperti nilai yang bukan `0` baik integer atau float, juga string yang bukan *empty string* dianggap sebagai nilai *Truthy*.

Kita bisa melakukan pengecekan terhadap suatu nilai, dan mengetahui ia nilai *truthy* atau *falsy* denga fungsi `bool()`. Secara eksplisit akan mengkonversi suatu nilai kedalam bentuk boolean dan mengembalikan nilainya. Dengan hal tersebut kita dapat mengetahui apakah nilai tersebut `truthy` atau `falsy`.

```python
print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False

print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True
```

Sekarang kita telah mengetahui apa itu nilai *Truthy* dan *Falsy*, selanjutnya kita akan membahas tentang operator boolean, dikenal juga dengan operator logika. Operator ini memungkinkan kita untuk melakukan operasi boolean kompleks dengan mengkombinasikan beberapa ekspresi secara bersamaan.

Tedapat tiga boolean operator di Python: `and`, `or` dan `not`.

Operator `and`, dengan operator ini kita harus memastikan kedua nilai atau ekspresi yang di operasikan harus menghasilkan nilai `True` atau *Truthy*. Jika salah satu saja ada yang bernilai `False` maka hasilnya akan false (salah).

```python
is_citizen = True
age = 25

if is_citizen and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')
```

Berkebalikan dengan `and`, untuk operator `or`, kita cukup memastikan salah satu nilai atau ekspresi saja yang bernilai `True`. Hasil akan tetap mengembalikan hasil *truthy* selagi salah satu nilai menghasilkan nilai `True`.

```python
age = 19
is_student = True

if age < 18 or is_student:
    print('You are eligible for a student discount') # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')
```

Operator `not` bersifat membalikan nilai, jika suatu nilai bersifat *truthy* maka akan dibalikan sebagai nilai *falsy*, begitpun dengan sebaliknya.

```python
print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy
```

```python
is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')
```

## Workshop: Membangun "Movie Ticket Booking Calculator"

```python
base_price = 15
age = 21
seat_type = "Gold"
show_time = "Evening"

if age > 17:
    print("User is eligible to book a ticket")

if age >= 21:
    print("User is eligible for Evening shows")
else:
    print("User is not eligible for Evening shows")

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print("User qualifies for membership discount")
else:
    print("User does not qualify for membership discount")
print("Discount:", discount)

extra_charges = 0
if is_weekend or show_time == "Evening":
    extra_charges = 2
    print("Extra charges will be applied")
else:
    print("No extra charges will be applied")
print("Extra charges:", extra_charges)

if age >= 21 or age >= 18 and (show_time != "Evening" or is_member):
    print("Ticket booking condition satisfied")
    service_charges = 0
    if seat_type == "Premium":
        service_charges = 5
    elif seat_type == "Gold":
        service_charges = 3
    else:
        service_charges = 1
    print("Service charges:", service_charges)
    final_price = base_price + extra_charges + service_charges - discount
    print("Final price of ticket:", final_price)
else:
    print("Ticket booking failed due to restrictions")
```

```terminal
User is eligible to book a ticket
User is eligible for Evening shows
User does not qualify for membership discount
Discount: 0
Extra charges will be applied
Extra charges: 2
Ticket booking condition satisfied
Service charges: 3
Final price of ticket: 20
```

## Lab: Membangun "Travel Weather Planner"

```python
distance_mi = 5
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = False

if not distance_mi:
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)
```

```terminal
True
```

## 1.6 Fungsi dan Cakupan ("Scope")

### Bagaimana Fungsi itu Bekerja di Python?

*Functions* adalah sebuah reusable code yang akan berjalan ketika dipanggil. Banyak bahasa pemrograman datang dengan fungsi bawaan masing-masing.

Salah satu fungsi bawaan yang paling berguna di Python selain `print()` adalah `input()`.

```python
name = input('What is your name?')
print('Hello', name)
```

Kita juga bisa menulis fungsi kustom. Untuk melakukannya, kita bisa menggunakan kata kunci `def`, diikuti nama fungsi yang ingin kita berikan kepada fungsi tersebut.

Berikut contohnya:

```python
def hello():
  print('Hello World')
```

Untuk menjalankan fungsi tersebut kita harus memanggilnya:

```python
hello()
```

Fungsi juga memerlukan indentasi dalam blok kode yang dibutuhkan.

Berikut merupakan fungsi sederhana untuk melakukan penjumlahan dari dua bilangan:

```python
def calculate_sum(a, b):
  print(a + b)

calculate_sum(3, 1)
```

Fungsi juga memiliki kata kunci khusus seperti `return`, secara umum jika kita tidak memberikan return terhadap fungsi, Python hanya mengembalikan `none`, sementara `return` akan mengembalikan nilai secara eksplisit.

```python
def calculate_sum(a, b):
  return a + b

my_sum = calculate_sum(3, 1)
print(my_sum)
```

### Apa itu "Scope" di Python dan Bagaimana Cara Kerjanya? 

Di Python, *scope* merupakan rangkaian bagaimana kita bisa memanggil sebuah variabel. 

Untuk menentukan cakupan dengan benar, Python mengikuti aturan LEGB, yang merupakan singkatan dari:

* **Local scope (L)**: Varibel yang didefinisikan dalam fungsi atau kelas.
* **Enclosing scope (E)**: Variabel yang didefinisikan dalam fungsi.
* **Global scope (G)**: Varibel yang didefinisikan pada tingkat teratas modul atau file.
* **Built-in scope (B)**: Nama-nama yang dicadangkan dalam Python untuk fungsi, modul, kata kunci dan objek yang telah ditentukan sebelumnya.

**Local Scope**, ketika sebuah variabel dideklarasikan di dalam sebuah fungsi, maka varibel tersebut hanya akan bisa dipanggil di dalam fungsi tersebut.

```python
def my_func():
  my_var = 10
  print(my_var)
```

**Enclosing scope**, berarti sebuah fungsi bersarang di dalam fungsi lain dapat mengakses variabel-variabel dari fungsi yang melingkupinya.

```python
def outer_func():
    msg = 'Hello there!'
    
    def inner_func():
        print(msg)
    
    inner_func()
    
outer_func()
```

Kita dapat menggunakan kata kunci `nonlocal`

```python
def outer_func():
    msg = 'Hello there!'
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal res  # Allow modification of an enclosing variable
        res = 'How are you?'
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(res)  # Now res is accessible and modified

outer_func()

# Output:
# Hello there!
# How are you?
```

**Global scope**, istilah merujuk pada varibel yang di deklarasikan di luar fungsi atau kelas apa pun dan dapat di akses dari mana saja dalam program. Di sini, 'my_var' dapat diakses di mana saja, bahkan di dalam fungsi yang tidak mendefinisikannya:

```python
my_var = 100

def show_var():
  print(my_var)

show_var()
print(my_var)
```

**built-in function**

```python
print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False
```

## Lab: Membangun "Apply Discount Function"

```python
def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return 'The price should be a number'
    
    if not isinstance(discount, (int, float)):
        return 'The discount should be a number'
    
    if price <= 0:
        return 'The price should be greater than 0'
    
    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
    
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    
    return final_price
```

## Workshop: Membangun "Caesar Cipher"

```python
def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return "Shift must be an integer value."

    if shift < 1 or shift > 25:
        return "Shift must be an integer between 1 and 25."

    if not encrypt:
        shift = -shift

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, False)


encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."

decrypted_text = decrypt(encrypted_text, 13)

print(decrypted_text)
```

## Lab: Membangun "RPG Character"

```python
def create_character(name, strength, intelligence, charisma):

    if not isinstance(name, str):
        return 'The character name should be a string'

    if name == '':
        return 'The character should have a name'

    if len(name) > 10:
        return 'The character name is too long'

    if ' ' in name:
        return 'The character name should not contain spaces'

    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return 'All stats should be integers'

    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'

    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'

    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'

    str_dots = '●' * strength + '○' * (10 - strength)
    int_dots = '●' * intelligence + '○' * (10 - intelligence)
    cha_dots = '●' * charisma + '○' * (10 - charisma)

    return f"""{name}
STR {str_dots}
INT {int_dots}
CHA {cha_dots}"""
```