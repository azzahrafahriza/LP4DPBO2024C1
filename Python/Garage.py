class Garage:
    def __init__(self, name, area):
        # Konstruktor kelas Garage
        self.__name = name      # Inisialisasi nama garasi
        self.__area = area      # Inisialisasi luas garasi
        self.__vehicles = []    # Inisialisasi daftar kendaraan yang diparkir di garasi

    def add_vehicle(self, vehicle):
        # Metode untuk menambahkan kendaraan ke dalam garasi
        self.__vehicles.append(vehicle)  # Menambahkan kendaraan ke dalam daftar kendaraan garasi

    def display_vehicles(self):
        # Metode untuk menampilkan kendaraan yang diparkir di garasi
        print(f"Kendaraan yang diparkir di {self.__name}:")  # Menampilkan informasi tentang kendaraan yang diparkir di garasi
        for vehicle in self.__vehicles:
            # Menggunakan perulangan untuk mencetak informasi tentang setiap kendaraan dalam daftar
            print(f"Nomor Plat : {vehicle.get_plate_number()}\n"
                  f"Merk       : {vehicle.get_brand()}\n"
                  f"Tahun      : {vehicle.get_year()}\n"
                  f"Warna      : {vehicle.get_color()}\n")
            # Menampilkan informasi tentang nomor plat, merek, tahun, dan warna kendaraan
