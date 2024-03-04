# LP4DPBO2024C1

## Janji 
Saya Azzahra Fahriza Fitriani NIM 2102296 mengerjakan soal Latihan Praktikum 4 dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin

![Uploading LP4.drawio.png…]()


## Kelas Vehicle
Kelas dasar atau superclass. Memiliki atribut-atribut umum untuk semua kendaraan.
Atribut:

- plat_nomor
- merk
- tahun_produksi
- warna

## Kelas Car
Subclass dari Vehicle. Menambahkan atribut khusus untuk mobil.
Atribut tambahan:

- jumlah_kursi
- jumlah_pintu

## Kelas Motorcycle
Subclass dari Vehicle. Menambahkan atribut khusus untuk sepeda motor.
Atribut tambahan:

- jenis_motor
- kapasitas_tangki

## Kelas ParkingLot
Kelas dasar atau superclass. Mewakili tempat parkir dengan kapasitas tertentu.
Atribut:

- kapasitas
- jumlah_kendaraan_saat_ini

## Kelas Garage
Subclass dari ParkingLot. Mewakili garasi tempat kendaraan diparkir. Menyimpan daftar kendaraan yang diparkir di dalamnya.
Atribut tambahan:

- nama_garasi
- luas_garasi
- daftar_kendaraan (list)


Garage akan memiliki daftar kendaraan yang diparkir di dalamnya. Ini menunjukkan hubungan komposisi antara Garage dan Vehicle.

## Alur Program:
1. Mulai program.
2. Import semua kelas yang diperlukan: Vehicle, Car, Motorcycle, Garage, dan ParkingLot.
3. Tentukan fungsi main() sebagai titik awal eksekusi program.
4.Buat objek kendaraan seperti mobil dan sepeda motor dengan atribut tertentu seperti plat nomor, merk, tahun produksi, warna, jumlah kursi, dan jumlah pintu.
5. Buat objek garasi dengan atribut nama garasi dan luas garasi.
6. Tambahkan kendaraan ke dalam garasi dengan menggunakan metode add_vehicle().
7. Tampilkan semua kendaraan yang diparkir di garasi dengan menggunakan metode display_vehicles().
8. Buat objek tempat parkir dengan kapasitas tertentu.
9. Parkirkan kendaraan di tempat parkir dengan menggunakan metode park_vehicle().

## Dokumen Python 
![image](https://github.com/azzahrafahriza/LP4DPBO2024C1/assets/101120742/bab7f6f3-e543-4236-b9a2-cdc26d606371)
