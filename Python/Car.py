from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, plate_number, brand, year, color, num_seats, num_doors):
        # Konstruktor kelas Car, mewarisi atribut dari kelas Vehicle
        super().__init__(plate_number, brand, year, color)
        self.__num_seats = num_seats    # Inisialisasi jumlah kursi
        self.__num_doors = num_doors    # Inisialisasi jumlah pintu

    def get_num_seats(self):
        # Metode untuk mendapatkan jumlah kursi
        return self.__num_seats

    def set_num_seats(self, num_seats):
        # Metode untuk mengatur jumlah kursi
        self.__num_seats = num_seats

    def get_num_doors(self):
        # Metode untuk mendapatkan jumlah pintu
        return self.__num_doors

    def set_num_doors(self, num_doors):
        # Metode untuk mengatur jumlah pintu
        self.__num_doors = num_doors
