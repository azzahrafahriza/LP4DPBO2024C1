from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, plat_nomor, merk, tahun_produksi, warna, jumlah_kursi, jumlah_pintu):
        super().__init__(plat_nomor, merk, tahun_produksi, warna)
        self.__jumlah_kursi = jumlah_kursi
        self.__jumlah_pintu = jumlah_pintu

    # Getter dan setter untuk jumlah_kursi
    def get_jumlah_kursi(self):
        return self.__jumlah_kursi

    def set_jumlah_kursi(self, jumlah_kursi):
        self.__jumlah_kursi = jumlah_kursi

    # Getter dan setter untuk jumlah_pintu
    def get_jumlah_pintu(self):
        return self.__jumlah_pintu

    def set_jumlah_pintu(self, jumlah_pintu):
        self.__jumlah_pintu = jumlah_pintu
