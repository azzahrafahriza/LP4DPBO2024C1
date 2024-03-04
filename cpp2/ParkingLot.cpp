#include <iostream>
#include <vector>
#include "Vehicle.cpp" // Saya asumsikan file ini mengandung implementasi kelas Vehicle

class ParkingLot {
private:
    int capacity;               // Kapasitas maksimum tempat parkir
    std::vector<Vehicle> vehicles; // Vektor untuk menyimpan daftar kendaraan yang diparkir

public:
    // Konstruktor untuk menginisialisasi objek ParkingLot dengan kapasitas dan daftar kendaraan kosong
    ParkingLot(int capacity) : capacity(capacity) {}

    // Getter untuk kapasitas tempat parkir
    int get_capacity() const {
        return capacity;
    }

    // Setter untuk kapasitas tempat parkir
    void set_capacity(int new_capacity) {
        capacity = new_capacity;
    }

    // Metode untuk memarkirkan kendaraan di tempat parkir
    void park_vehicle(Vehicle vehicle) {
        if (vehicles.size() < capacity) {  // Memeriksa apakah ada ruang kosong di tempat parkir
            vehicles.push_back(vehicle);   // Menambahkan kendaraan ke daftar kendaraan yang diparkir
            std::cout << vehicle.get_plate_number() << " berhasil diparkir!" << std::endl;  // Mencetak pesan sukses
        } else {
            std::cout << vehicle.get_plate_number() << " tidak dapat parkir karena tempat parkir penuh!" << std::endl; // Mencetak pesan yang menunjukkan tempat parkir penuh
        }
    }

    // Metode untuk menampilkan detail kendaraan yang diparkir di tempat parkir
    void display_parked_vehicles() {
        std::cout << "Kendaraan yang diparkir di tempat parkir:" << std::endl;
        for (const auto& vehicle : vehicles) { // Mengulangi daftar kendaraan yang diparkir
            std::cout << "Nomor Plat: " << vehicle.get_plate_number() << std::endl;   // Mencetak nomor plat kendaraan
            std::cout << "Merk      : " << vehicle.get_brand() << std::endl;          // Mencetak merk kendaraan
            std::cout << "Tahun     : " << vehicle.get_year() << std::endl;           // Mencetak tahun kendaraan
            std::cout << "Warna     : " << vehicle.get_color() << std::endl;          // Mencetak warna kendaraan
        }
    }
};
