class Vehicle:
    def __init__(self, plate_number, brand, year, color):
        # Konstruktor kelas Vehicle, menerima parameter plat nomor, merk, tahun produksi, dan warna
        self.__plate_number = plate_number   # Inisialisasi plat nomor
        self.__brand = brand                 # Inisialisasi merk
        self.__year = year                   # Inisialisasi tahun produksi
        self.__color = color                 # Inisialisasi warna

    def get_plate_number(self):
        # Metode untuk mendapatkan plat nomor kendaraan
        return self.__plate_number

    def set_plate_number(self, plate_number):
        # Metode untuk mengatur plat nomor kendaraan
        self.__plate_number = plate_number

    def get_brand(self):
        # Metode untuk mendapatkan merk kendaraan
        return self.__brand

    def set_brand(self, brand):
        # Metode untuk mengatur merk kendaraan
        self.__brand = brand

    def get_year(self):
        # Metode untuk mendapatkan tahun produksi kendaraan
        return self.__year

    def set_year(self, year):
        # Metode untuk mengatur tahun produksi kendaraan
        self.__year = year

    def get_color(self):
        # Metode untuk mendapatkan warna kendaraan
        return self.__color

    def set_color(self, color):
        # Metode untuk mengatur warna kendaraan
        self.__color = color
