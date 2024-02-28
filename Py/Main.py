from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle
from Garage import Garage
from ParkingLot import ParkingLot

def main():
    # Create vehicles
    car1 = Car("ABC123", "Toyota", 2022, "Red", 5, 4)
    motorcycle1 = Motorcycle("XYZ456", "Honda", 2021, "Black", "Sport", 10)
    vehicle1 = Vehicle("LMN789", "Ford", 2020, "Blue")


    car2 = Car("DEF456", "Xenia", 2024, "Pink", 5, 4) # Membuat objek mobil dengan atribut tertentu
    motorcycle2 = Motorcycle("LKJ789", "Yamahaha", 2023, "White", "Sport", 6) # Membuat objek sepeda motor dengan atribut tertentu
    # Create garage
    garage = Garage("Garasi Jara", 100)

    # Add vehicles to garage
    garage.add_vehicle(car1)
    garage.add_vehicle(motorcycle1)
    garage.add_vehicle(vehicle1)

    garage.add_vehicle(car2)
    garage.add_vehicle(motorcycle2)

    # Display vehicles in garage
    garage.display_vehicles()

    # Create parking lot
    parking_lot = ParkingLot(2)

    # Park vehicles in parking lot
    parking_lot.park_vehicle(car1)
    parking_lot.park_vehicle(motorcycle1)
    parking_lot.park_vehicle(vehicle1)

if __name__ == "__main__":
    main()
