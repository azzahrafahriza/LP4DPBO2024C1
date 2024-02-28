from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, plate_number, brand, year, color, type_motor, tank_capacity):
        # Konstruktor kelas Motorcycle, mewarisi atribut dari kelas Vehicle
        super().__init__(plate_number, brand, year, color)
        self.__type_motor = type_motor        # Inisialisasi jenis motor
        self.__tank_capacity = tank_capacity  # Inisialisasi kapasitas tangki bahan bakar

    def get_type_motor(self):
        # Metode untuk mendapatkan jenis motor
        return self.__type_motor

    def set_type_motor(self, type_motor):
        # Metode untuk mengatur jenis motor
        self.__type_motor = type_motor

    def get_tank_capacity(self):
        # Metode untuk mendapatkan kapasitas tangki bahan bakar
        return self.__tank_capacity

    def set_tank_capacity(self, tank_capacity):
        # Metode untuk mengatur kapasitas tangki bahan bakar
        self.__tank_capacity = tank_capacity
