#include <iostream>
#include <string>
#include <vector>
#include "Vehicle.cpp" // Include header file Vehicle.h

class Garage {
private:
    std::string name;
    double area;
    std::vector<Vehicle> vehicles; // Vektor untuk menyimpan daftar kendaraan yang diparkir di garasi

public:
    // Konstruktor untuk kelas Garage
    Garage(std::string name, double area) : name(name), area(area) {}

    // Metode untuk menambahkan kendaraan ke dalam garasi
    void add_vehicle(Vehicle vehicle) {
        vehicles.push_back(vehicle);
    }

    // Metode untuk menampilkan kendaraan yang diparkir di garasi
    void display_vehicles() {
        std::cout << "Kendaraan yang diparkir di " << name << ":" << std::endl;
        for (const auto& vehicle : vehicles) {
            std::cout << "Nomor Plat : " << vehicle.get_plate_number() << std::endl;
            std::cout << "Merk       : " << vehicle.get_brand() << std::endl;
            std::cout << "Tahun      : " << vehicle.get_year() << std::endl;
            std::cout << "Warna      : " << vehicle.get_color() << std::endl;
            std::cout << std::endl;
        }
    }
};