class ParkingLot:
    def __init__(self, capacity):
        # Konstruktor untuk menginisialisasi objek ParkingLot dengan kapasitas dan daftar kendaraan kosong
        self.__capacity = capacity  # Menetapkan kapasitas maksimum dari tempat parkir
        self.__vehicles = []        # Menginisialisasi sebuah daftar kosong untuk menyimpan kendaraan yang diparkir
    
    def park_vehicle(self, vehicle):
        # Metode untuk memarkirkan kendaraan di tempat parkir
        if len(self.__vehicles) < self.__capacity:  # Memeriksa apakah ada ruang kosong di tempat parkir
            self.__vehicles.append(vehicle)        # Menambahkan kendaraan ke daftar kendaraan yang diparkir
            
            print(f"{vehicle.get_plate_number()} berhasil diparkir!")  # Mencetak pesan sukses
        else:
            print(f"{vehicle.get_plate_number()} tidak dapat parkir karena tempat parkir penuh!")         # Mencetak pesan yang menunjukkan tempat parkir penuh
    
    def display_parked_vehicles(self):
        # Metode untuk menampilkan detail kendaraan yang diparkir di tempat parkir
        
        print("Kendaraan yang diparkir di tempat parkir:")
        for vehicle in self.__vehicles:                             # Mengulangi daftar kendaraan yang diparkir
            print(f"Nomor Plat: {vehicle.get_plate_number()}\n"     # Mencetak nomor plat kendaraan
                  f"Merk      : {vehicle.get_brand()}\n"                   # Mencetak merk kendaraan
                  f"Tahun     : {vehicle.get_year()}\n"                  # Mencetak tahun kendaraan
                  f"Warna     : {vehicle.get_color()}\n")                  # Mencetak warna kendaraan
