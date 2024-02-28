# Import kelas-kelas yang diperlukan dari modul yang sesuai
from Vehicle import Vehicle       # Import kelas Vehicle dari modul Vehicle
from Car import Car               # Import kelas Car dari modul Car
from Motorcycle import Motorcycle # Import kelas Motorcycle dari modul Motorcycle
from Garage import Garage         # Import kelas Garage dari modul Garage
from ParkingLot import ParkingLot # Import kelas ParkingLot dari modul ParkingLot

def main():
    # Membuat objek kendaraan
    car1 = Car("ABC123", "Toyota", 2022, "Red", 5, 4) # Membuat objek mobil dengan atribut tertentu
    motorcycle1 = Motorcycle("XYZ456", "Honda", 2025, "Black", "Sport", 10) # Membuat objek  motor dengan atribut tertentu

    car2 = Car("DEF456", "Xenia", 2024, "Pink", 5, 4) # Membuat objek mobil dengan atribut tertentu
    motorcycle2 = Motorcycle("LKJ789", "Yamahaha", 2023, "White", "Sport", 6) # Membuat objek sepeda motor dengan atribut tertentu
    # Membuat objek garasi
    garage = Garage("garasi jara", 100) # Membuat objek garasi dengan nama "jara's garage" dan kapasitas maksimum 100

    # Menambahkan kendaraan ke garasi
    print("======================================================\n")
    garage.add_vehicle(car1)        # Menambahkan mobil ke garasi
    garage.add_vehicle(motorcycle1) # Menambahkan  motor ke garasi

    garage.add_vehicle(car2)        # Menambahkan mobil ke garasi
    garage.add_vehicle(motorcycle2) # Menambahkan  motor ke garasi

    garage.add_vehicle(Car("HJK885", "Jondo", 2022, "Yellow", 8, 4))        # Menambahkan mobil ke garasi
    garage.add_vehicle(Motorcycle("YTR669", "Vespa", 2024, "Black", "Naked", 10)) # Menambahkan  motor ke garasi

    # Menampilkan kendaraan yang ada di garasi
    garage.display_vehicles()        # Menampilkan informasi tentang kendaraan yang ada di garasi

    # Membuat objek tempat parkir
    parking_lot = ParkingLot(2)      # Membuat objek tempat parkir dengan kapasitas maksimum 5 kendaraan

    # Memarkirkan kendaraan di tempat parkir
    print("======================================================\n")
    parking_lot.park_vehicle(car1)               # Memarkirkan mobil di tempat parkir
    parking_lot.park_vehicle(motorcycle1)        # Memarkirkan  motor di tempat parkir
    parking_lot.park_vehicle(Vehicle("LMN789", "Ford", 2020, "Blue")) # Memarkirkan kendaraan lain di tempat parkir

    # Menampilkan kendaraan yang diparkir di tempat parkir
    print("\n======================================================\n")
    parking_lot.display_parked_vehicles()        # Menampilkan informasi tentang kendaraan yang diparkir di tempat parkir

if __name__ == "__main__":
    main()
