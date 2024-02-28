from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, plat_nomor, merk, tahun_produksi, warna, jenis_motor, kapasitas_tangki):
        super().__init__(plat_nomor, merk, tahun_produksi, warna)
        self.__jenis_motor = jenis_motor
        self.__kapasitas_tangki = kapasitas_tangki

    # Getter dan setter untuk jenis_motor
    def get_jenis_motor(self):
        return self.__jenis_motor

    def set_jenis_motor(self, jenis_motor):
        self.__jenis_motor = jenis_motor

    # Getter dan setter untuk kapasitas_tangki
    def get_kapasitas_tangki(self):
        return self.__kapasitas_tangki

    def set_kapasitas_tangki(self, kapasitas_tangki):
        self.__kapasitas_tangki = kapasitas_tangki
