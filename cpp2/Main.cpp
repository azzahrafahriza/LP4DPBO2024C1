#include <iostream>
#include <vector>
#include "Vehicle.cpp" // Saya asumsikan file ini mengandung implementasi kelas Vehicle
#include "Car.cpp"     // Saya asumsikan file ini mengandung implementasi kelas Car
#include "Motorcycle.cpp" // Saya asumsikan file ini mengandung implementasi kelas Motorcycle
#include "Garage.cpp"  // Saya asumsikan file ini mengandung implementasi kelas Garage
#include "ParkingLot.cpp" // Saya asumsikan file ini mengandung implementasi kelas ParkingLot

int main() {
    // Membuat objek kendaraan
    Car car1("ABC123", "Toyota", 2022, "Red", 5, 4); // Membuat objek mobil dengan atribut tertentu
    Motorcycle motorcycle1("XYZ456", "Honda", 2025, "Black", "Sport", 10); // Membuat objek motor dengan atribut tertentu

    Car car2("DEF456", "Xenia", 2024, "Pink", 5, 4); // Membuat objek mobil dengan atribut tertentu
    Motorcycle motorcycle2("LKJ789", "Yamahaha", 2023, "White", "Sport", 6); // Membuat objek sepeda motor dengan atribut tertentu

    // Membuat objek garasi
    Garage garage("garasi jara", 100); // Membuat objek garasi dengan nama "jara's garage" dan kapasitas maksimum 100

    // Menambahkan kendaraan ke garasi
    std::cout << "======================================================\n";
    garage.add_vehicle(car1);        // Menambahkan mobil ke garasi
    garage.add_vehicle(motorcycle1); // Menambahkan motor ke garasi
    garage.add_vehicle(car2);        // Menambahkan mobil ke garasi
    garage.add_vehicle(motorcycle2); // Menambahkan motor ke garasi
    garage.add_vehicle(Car("HJK885", "Jondo", 2022, "Yellow", 8, 4));        // Menambahkan mobil ke garasi
    garage.add_vehicle(Motorcycle("YTR669", "Vespa", 2024, "Black", "Naked", 10)); // Menambahkan motor ke garasi

    // Menampilkan kendaraan yang ada di garasi
    garage.display_vehicles();        // Menampilkan informasi tentang kendaraan yang ada di garasi

    // Membuat objek tempat parkir
    ParkingLot parking_lot(2);      // Membuat objek tempat parkir dengan kapasitas maksimum 5 kendaraan

    // Memarkirkan kendaraan di tempat parkir
    std::cout << "======================================================\n";
    parking_lot.park_vehicle(car1);               // Memarkirkan mobil di tempat parkir
    parking_lot.park_vehicle(motorcycle1);        // Memarkirkan motor di tempat parkir
    parking_lot.park_vehicle(Vehicle("LMN789", "Ford", 2020, "Blue")); // Memarkirkan kendaraan lain di tempat parkir

    // Menampilkan kendaraan yang diparkir di tempat parkir
    std::cout << "\n======================================================\n";
    parking_lot.display_parked_vehicles();        // Menampilkan informasi tentang kendaraan yang diparkir di tempat parkir

    return 0;
}
