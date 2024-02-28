class Garage:
    def __init__(self, nama_garasi, luas_garasi):
        self.__nama_garasi = nama_garasi
        self.__luas_garasi = luas_garasi
        self.__daftar_kendaraan = []

    # Getter dan setter untuk nama_garasi
    def get_nama_garasi(self):
        return self.__nama_garasi

    def set_nama_garasi(self, nama_garasi):
        self.__nama_garasi = nama_garasi

    # Getter dan setter untuk luas_garasi
    def get_luas_garasi(self):
        return self.__luas_garasi

    def set_luas_garasi(self, luas_garasi):
        self.__luas_garasi = luas_garasi

    # Getter dan setter untuk daftar_kendaraan
    def get_daftar_kendaraan(self):
        return self.__daftar_kendaraan

    def set_daftar_kendaraan(self, daftar_kendaraan):
        self.__daftar_kendaraan = daftar_kendaraan

    # Metode untuk menambahkan kendaraan ke daftar
    def add_vehicle(self, vehicle):
        self.__daftar_kendaraan.append(vehicle)

    # Metode untuk menampilkan kendaraan dalam garasi
    def display_vehicles(self):
        print(f"Kendaraan yang diparkir di {self.__nama_garasi}:")
        for vehicle in self.__daftar_kendaraan:
            print(f"Plat Nomor: {vehicle.get_plat_nomor()}\n"
                  f"Merk      : {vehicle.get_merk()}\n"
                  f"Tahun     : {vehicle.get_tahun_produksi()}\n"
                  f"Warna     : {vehicle.get_warna()}\n")
