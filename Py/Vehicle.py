class Vehicle:
    def __init__(self, plat_nomor, merk, tahun_produksi, warna):
        self.__plat_nomor = plat_nomor
        self.__merk = merk
        self.__tahun_produksi = tahun_produksi
        self.__warna = warna

    # Getter dan setter untuk plat_nomor
    def get_plat_nomor(self):
        return self.__plat_nomor

    def set_plat_nomor(self, plat_nomor):
        self.__plat_nomor = plat_nomor

    # Getter dan setter untuk merk
    def get_merk(self):
        return self.__merk

    def set_merk(self, merk):
        self.__merk = merk

    # Getter dan setter untuk tahun_produksi
    def get_tahun_produksi(self):
        return self.__tahun_produksi

    def set_tahun_produksi(self, tahun_produksi):
        self.__tahun_produksi = tahun_produksi

    # Getter dan setter untuk warna
    def get_warna(self):
        return self.__warna

    def set_warna(self, warna):
        self.__warna = warna
