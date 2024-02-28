class ParkingLot:
    def __init__(self, kapasitas):
        self.__kapasitas = kapasitas
        self.__jumlah_kendaraan_saat_ini = 0

    # Getter dan setter untuk kapasitas
    def get_kapasitas(self):
        return self.__kapasitas

    def set_kapasitas(self, kapasitas):
        self.__kapasitas = kapasitas

    # Getter dan setter untuk jumlah_kendaraan_saat_ini
    def get_jumlah_kendaraan_saat_ini(self):
        return self.__jumlah_kendaraan_saat_ini

    def set_jumlah_kendaraan_saat_ini(self, jumlah_kendaraan_saat_ini):
        self.__jumlah_kendaraan_saat_ini = jumlah_kendaraan_saat_ini

    # Metode untuk memarkirkan kendaraan
    def park_vehicle(self, vehicle):
        if self.__jumlah_kendaraan_saat_ini < self.__kapasitas:
            self.__jumlah_kendaraan_saat_ini += 1
            print(f"{vehicle.get_plat_nomor()} berhasil diparkir!")
        else:
            print("Tempat parkir penuh!")
