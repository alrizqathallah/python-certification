# Level 3: OOP

## Topik 1: Basic OOP (Class dan Object)

Sekarang kita memasuki duni **OOP** (*Object Oriented Programming*) atau Pemrograman Berorientasi Objek. Ini adalah cara para programmer profesional menyusun kode untuk aplikasi skala besar (seperti game, sistem bank, atau media sosial).

Mari kita guanakn analogi dunia nyata:

Bayangkan sebuah **Class** (Kelas) sebagai **cetakan kue** atau **blue print (cetak biru) arsitektur rumah**. Cetakan itu sendiri bukanlah kue yang bisa dimakan, melainkan cetakan yang menentukan *bentuk* dan *fitur* kue tersebut.

Sedangkan **Object** (Objek) adalah **kue asli** yang dicetak dari cetakan tersebut. Dari satu cetakan yang sama, kita bisa membuat banyak kue dengan warna atau rasa yang berbeda-beda.

Di Python, kita membuat cetakan tersebut dengan kata kunci `class`:

```Python
# Membuat "Cetakan" bernama Robot
class Robot:
  pass # pass digunakan sementara jika isi class masih kosong
```

Untuk membuat "Objek nyata" dari cetakan tersebut, caranya seperti ini:

```Python
robot_saya = Robot()  # robot_saya sekarang adalah sebuah Objek
```

**Tantangan OOP Pertama**

Mari kita coba membuat cetakan pertama.

Coba buat kode yang:

1. Buat sebuah Class bernama `Mobil`.
2. Dibawahnya (di luar class), buat sebuah objek bernama `mobil_iky` yang dicetak dari Class `Mobil` tersebut.

**Jawaban**:

```Python
# Tantangan OOP pertama
class Mobil:
    pass

mobil_iky = Mobil()
```

**Pembahasan**: 

Kita sudah berhasil membuat cetakan (`Class`) bernama `Mobil` dan mencetak sebuah objek nyata bernama `mobil_iky` dari cetakan tersebut.

Meskipun mobil tersebut saat ini masih kosong (belum punya warna, merek, atau kemampuan untuk berjalan), fondasi yang kita buat sudah sangat benar.

### Constructor (`__init__`) dan Atribut

Sekarang, mari kita beri "isi" dan karakteristik pada cetakan mobil kita. Di dunia nyata, setiap mobil pasti punya karakteristik spesifik seperti **merek**, **warna**, dan **kecepatan**. Di dalam OOP, karakteristik ini disebut **Atribut**.

Untuk memasukkan atribut ini saat objek pertama kali dibuat, kita menggunakan fungsi khusus yang disebut **Constructor**. Di Python, namanya ditulis dengan tanda `def __init__(self,...)` (menggunakan garis bawah atau *underscore* di dapan dan dibelakang).

Mari kita bedah contoh di bawah ini:

```Python
class Mobil:
    # Constructor untuk menyiapkan data awal mobil
    def __init__(self, merek, warna):
        self.merek = merek  # Menyimpan merek ke dalam mobil ini
        self.warna = warna  # Menyimpan warna ke dalam mobil ini

# Sekarang saat mencetak mobil, kita harus memasukkan merek dan warnanya
mobil_iky = Mobil("Toyota", "Hitam")
mobil_budi = Mobil("Honda", "Merah")

# Cara mengakses atributnya
print(mobil_iky.merek)  # Hasilnya: Toyota
print(mobil_budi.warna) # Hasilnya: Merah
```

**Apa itu `self`?**

Bayangkan `self` sebagai kata ganti "ini" atau "milik saya". Saat `mobil_iky` dibuat, `self.merek` berarti "Merek milik mobil *ini* adalah Toyota". `self` membantu Python membedakan dat antara `mobil_iky` dan `mobil_budi` agar tidak tertukar meskipun berasal dari cetakan yang sama.

### Tantangan Constructor dan Atribut

Mari kita praktikkan konsep ini pada objek yang berbeda.

Coba buat kode yang:

1. Buat seubah Class bernama `Kucing`.
2. Buat fungsi `__init__` (Constructor) yang menerima dua parameter atribut: `nama` dan `ras`.
3. Di luar class, buat sebuah objek bernama `kucing_saya` denga nama `"Meong"` dan ras `"Anggora"`.
4. Tampilkan data tersebut menggunakan f-string dengan format seperti in: `"Kucing saya bernama Meong dan dia adalah ras Anggora"`.

**Jawaban**:

```Python
class Kucing:
    def __init__(self, nama, ras):
        self.nama = nama
        self.ras = ras
        
kucing_saya = Kucing("Meong", "Anggora")

print(f"Kucing saya bernaama {kucing_saya.nama} dan dia adalah ras {kucing_saya.ras}.")
```

```Terminal
Kucing saya bernaama Meong dan dia adalah ras Anggora.
```

**Pembahasan**:

Kita telah membuat Class `kucing`, mendefinisikan *constructor* `__init__` dengan benar menggunakan `self`, membuat objek `kucing_saya`, dan mengakses atributnya menggunakan f-string. Pemahaman kita tentang dasar OOP ini sudah sangat kuat.

### Method (Fungsi di dalam Class)

Sekarang, sebuah objek tidak hanya memiliki karkateristik (Atribut) tapi juga harus bisa melakukan sesuatu (Aksi/Perilaku). Di dalam OOP, fungsi yagn diletakkan di dalam Class dan mendefinisikan perilaku dari objek tersebut disebut dengan **Method**.

Sama seperti fungsi biasa, kita membuatnya dengan kata kunci `def`, dan wajib memasukkan `self` sebagai parameter pertamanya agar method tersebut tahu objek mana yang sedang melakukan aksi.

Mari kita tambahnkan perilaku pada Class `Kucing` kita:

```Python
class Kucing:
  def __init__(self, nama, ras):
    self.nama = nama
    self.ras = ras

  # Ini adalah Method (Perilaku si kucing)
  def bersuara(self):
    print(f"{self.nama} berkata: Meong... Miaw!")
```

Cara memanggil method tersebut mirip dengan cara mengambil atribut, yaitu menggunakan tanda titik (`.`), diikuti dengan nama method dan tanda kurung `()`:

```Python
kucing_saya = Kucing("Meong", "Anggora")
kucing_saya.bersuara()  # Hasil di layar: Meong berkata: Meong... Miaw!
```

### Tantangan Method

Mari kita buat sebuah objek yang bisa melakukan perhitungan matematika melalui method-nya.

Coba buat kode yang:

1. Buat sebuah Class bernama `Kalkulator`.
2. Class ini tidak perlu `__init__` (kosongkan saja data awalnya, langsung buat method)
3. Buat sebuah method di dalamnya bernama `tambah` yang menerima parameter `self`, `angka1`, dan `angka2`.
4. Di dalam method tersebut, kembalikan (`return`) hasil penjumlahan dari `angka1` dan `angka2`.
5. Di luar Class, buat objek bernama `hitung`, lalu panggil method `tambah` dengan memasukkan angka `10` dan `5`. Tampilkan hasilnya ke layar.

**Jawaban**:

```Python
# Tantangan Method
class Kalkulator:
    def tambah(self, angka1, angka2):
        return angka1 + angka2

angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))

hitung = Kalkulator()

hasil_penjumlahan = hitung.tambah(angka1, angka2)

print(f"Hasil penjumlahan dari {angka1} ditambah {angka2} adalah: {hasil_penjumlahan}")
```

```Terminal
Masukkan angka pertama: 10
Masukkan angka kedua: 5
Hasil penjumlahan dari 10 ditambah 5 adalah: 15
```

**Pembahasan**:

Kita menuliskan strukturnya dengan sangat rapi dan lagi-lagi berimprovisasi menggunakan `input()` dan *casting* `int()`.

Kita juga sudah sangat tepat dalam memanggil method `hitung.tambah(angka1, angka2)`.
Perhatikan bagaimana kita tidak perlu memasukkan data untuk parameter `self` saat memanggilnya, karena Python secara otomatis mengisi `self` dengan objek `hitung` itu sendiri.

## Topik 2: Pilar OOP - Inheritance (Pewarisan)

Dalam dunia nyata, seorang anak bisa mewarisi sifat atau aset dari orang tuanya. Di dalam OOP sebuah Class bisa mewarisi atribut dan method dari Class lain yang sudah ada.

* **Parent Class (Kelas Induk)**: Kelas yang menurunkan sifat.
* **Child Class (Kelas Anak)**: Kelas yang menerima warisan. Dia otomatis mendapatkan semua kemampuan bapaknya, plus bisa punya kemampuan unik sendiri yang tidak dimiliki bapaknya.

Cara melakukan di Python adalah dengan memasukkan nama kelas induk ke dalam tanda kurung saat membuat kelas anak.

Mari perhatikan contoh ini:

```Python
# Kelas Induk
class Hewan:
  def __init__(self, nama):
    self.nama = nama
  
  def makan(self):
    print(f"{self.nama} sedang makan... Nyam!")

# Kelas Anak (Mearisi Hewan)
class Burung(Hewan):
  def terbang(self):
    print(f"{self.nama} terbang tinggi di langit!")

# Uji Coba
merpati = Burung("Beni")
merpati.makan()     # BISA! Warisan dari kelas hewan
merpati.terbang( )  # BISA! Kemampuan unik kelas Burung sendiri
```

### Tantangan Inheritance

Mari kita sistem kendaraan sederhana.

Cobalah buat kode yang:

1. Buat Parent Class bernama `kendaraan` yang memiliki `__init__` dengan atribut `merek`.
2. Di dalam kendaraan, buat method bernama `klakson` yang mencetak `"Biiip booop!"`.
3. Buat Child Class bernama `Motor` yang mewarisi (inherit) dari `Kendaraan`. Di dalam `Motor`, buat method unik bernama `wheelie` yang mencetak `"Motor standing tinggi!"`.
4. Di luar class, buat objek dari kelas `Motor` dengan merek `"Yamaha"`, lalu panggil method `klakson` dan method `wheelie`-nya.

**Jawaban**:

```Python
# Tantangan INHERITANCE
class Kendaraan:
    def __init__(self, merek):
        self.merek = merek
    
    def klakson(self):
        print("Biiip booop!")

class Motor(Kendaraan):
    def wheelie(self):
        print("Motor standing tinggi!")

roda_dua = Motor("Yamaha")
print(f"Motor baru saya: {roda_dua.merek}")
roda_dua.klakson()
roda_dua.wheelie()
```

```Terminal
Motor baru saya: Yamaha
Biiip booop!
Motor standing tinggi!
```

**Pembahasan**:

Hubungan pewarisan (*inheritance*) antara `Kendaraan` sebagai induk dan `Motor` sebagai anak sudha kita terapkan dengan sangat tepat.

Objek `roda_dua` yang merupakan instansiasi dari kelas `Motor` terbukti bisa mengakses atribut `merek` dan method `klakson` dari kelas induknya, sekaligus menjalankan method uniknya sendiri, yaitu `wheelie`. Skrip dan logika yang kita tulis benar-benar mantap!

## Topik 3: Polymorphism (Banyak Bentuk)

Kata *Polymorphism* berasal dari bahasa Yunani yang berarti **"banyak bentuk"**. Dalam pemrograman OOP, konsep ini memungkinkan kita menggunakan satu nama method yang sama di berbagai kelas yang berbeda, tetapi setiap kelas tersebut memberikan hasil atau perilaku yang berbeda pula.

Cara paling umu untuk melakukan ini adalah melalui **Method Overriding** (mengganti atau menimpa method milik induk dengan cara si anak sendiri).

Mari perhatikan contoh ini:

```Python
class Kucing:
  def bersuara(self):
    print("Meong!")

class Anjing:
  def bersuara(self):
    print("Guk guk!)

hewan1 = Kucing()
hewan2 = Anjing()

hewan1.bersuara()
hewan2.bersuara()
```

Kenapa ini keren? Karena kita bisa membuat sebuah fungsi universal yang bisa menyuruh hewan apa pun untuk bersuara tanpa perlu tahu apa jenis hewannya terlebih dahulu!

### Tantangan Polymorphism

Mari kita buat simulasi sistem pembayaran toko online

Coba buat kode yang:

1. Buat sebuah Class bernama `Ovo` yang memiliki method `bayar(self, jumlah)`. Di dalamnya cetak pesan: `Membayar menggunakan Ovo sebesar Rp {jumlah}`.
2. Buat Class bernama `Gopay` yang juga memiliki method dengan nama yang persis sama, yaitu `bayar(self, jumlah)`. Di dalamnya, cetak pesan: `Membayar menggunakan Gopay sebesar Rp {jumlah}`.
3. Di luar class, buat objek untuk masing-masing kelas, lalu panggil method `bayar` dengan memasukkan angka `50000` pada kedua objek tersebut.

**Jawaban**:

```Python
# Tantangan POLYMORPHISM
class Ovo:
    def bayar(self, jumlah):
        print(f"Membayar menggunakan Ovo sebesar Rp {jumlah}")
        
class Gopay:
    def bayar(self, jumlah):
        print(f"Membayar menggunakan Gopay sebesar Rp {jumlah}")
        
pembayaran_ovo = Ovo()
pembayaran_gopay = Gopay()

nominal_pembayaran = input("Masukkan nominal pembayaran: ")

pembayaran_ovo.bayar(nominal_pembayaran)
pembayaran_gopay.bayar(nominal_pembayaran)
```

```Terminal
Masukkan nominal pembayaran: 50000
Membayar menggunakan Ovo sebesar Rp 50000
Membayar menggunakan Gopay sebesar Rp 50000
```

**Pembahasan**:

Kita berhasil menerapkan konsep *Polymorphism* dengan sangat baik.

Meskipun objek `pembayaran_ovo` dan `pembayaran_gopay` berasal dari kelas yang berbeda, keduanya bisa merespons perintah dengan naam method yang sama (`.bayar()`) namun menghasilkan aksi yang berbeda sesuai dengan karakteristik kelasnya masing-masing.
Improvisasi pengambilan input nominal dari pengguna juga membuat kodenya terasa seperti sistem pembayaran asli!

## Topik 4: Encapsulation (Penyembunyian Data)

*Encapsulation* (Pengapsulan) adalah konsep untuk membungkus data dan **menyembunyikan** atribut atau method di dalam objek agar tidak bisa diubah-ubah secara sembarangan dari luar kelas. Ini demi alasan keamanan data.

Bayangkan seperti saldo rekening bank milik kita. Orang luar tidak boleh bisa langsung mengubah angka saldo tersebut seperti `rekening.saldo = 1000000000`. Perubahan saldo harus melalui prosedur yang aman (sperti menabung atau menarik uang).

Di Python, kita menyembunyikan atribut dengan menambahkan **dua tanda garis bawah (double *underscore*)** didepan nama atributnya. Ini akan membuat atribut tersebut bersifat **Private**.

Mari perhatikan perbedaan ini:

```Python
class AkunBank:
  def __init__(self, nama, saldo_awal):
    self.nama - nama
    self.__saldo = saldo_awal # Atribut PRIVATE kerena pakai __

akun_iky = AkunBank("Iky", 50000)

print(akun_iky.nama)    # BISA diakses: Hasilnya Iky
print(akun_iky.__saldo) # ERROR! Python akan memproteksinya dan berteriak AttributeError
```

**Bagaimaan cara mengakses atau mengubah data Private?**

Kita menggunakan method khusus di dalam kelas yang disebut **Getter** (untuk mengambil/melihat nilai) dan **Setter** (untuk mengubah nilai dengan variabel).

```Python
class AkunBank:
    def __init__(self, nama, saldo_awal):
        self.nama = nama
        self.__saldo = saldo_awal

    # GETTER: Method untuk mengintip saldo secara aman
    def cek_saldo(self):
        return self.__saldo

    # SETTER: Method untuk mengubah saldo secara aman
    def isi_saldo(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah harus lebih dari 0!")
```

### Tantangan Encapsulation & Penutup Level 3

Mari kita buat sistem keamanan data akun pengguna sederhana.

Coba buat kode yang:

1. Buat Class bernama `Akun`.
2. Di dalam `__init__`, buat atribut biasa bernama `username` dan buat atribut **Private** bernama `__password`.
3. Buat sebuah method **Getter** bernama `lihat_password(self)` yang mengembalikan (*return*) nilai dari `__password`.
4. Di luar class, buat objek dari kelas `Akun`, lalu coba tampilkan password-nya menggunakan bantuan method Getter tersebut.

**Jawaban**:

```Python
# Tantangan Encapsulation & Penutup Level 3
# 1. Membuat Class bernama Akun
class Akun:
    def __init__(self, username, password):
        self.username = username  # Atribut Publik (Bisa diakses siapa saja)
        self.__password = password  # Atribut Private (Terkunci di dalam kelas)

    # 2. Membuat Method Getter untuk mengambil data secara aman
    def lihat_password(self):
        # Kita bisa menambahkan logika pengecekan di sini jika mau
        return self.__password


# 3. Membuat Objek dari kelas Akun
akun_user = Akun("budi_ganteng", "Rahasia123!")

# 4. Mencoba mengakses data
print("Username:", akun_user.username)

# Mengakses password menggunakan bantuan Getter
print("Password (via Getter):", akun_user.lihat_password())
```

```Terminal
Username: budi_ganteng
Password (via Getter): Rahasia123!
```

**Pembahasan**:

Penerapan *Encapsulation* kita sangat matang. Komentar kita didalam kode juga menunjukkan bahwa kita sudah benar-benar paham esensi dari enkapsulasi: menyembunyikan dat sensitif (`__password`) dan menyediakan gerbang masuk yang aman lewat *Getter* (`lihat_password()`).

