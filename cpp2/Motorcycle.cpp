#include <iostream>
#include <string>
#include "Vehicle.cpp" // Include header file Vehicle.h

class Motorcycle : public Vehicle { // Menurunkan kelas Motorcycle dari kelas Vehicle
private:
    std::string type_motor;
    int tank_capacity;

public:
    // Konstruktor untuk kelas Motorcycle
    Motorcycle(std::string plate_number, std::string brand, int year, std::string color, std::string type_motor, int tank_capacity)
        : Vehicle(plate_number, brand, year, color), type_motor(type_motor), tank_capacity(tank_capacity) {}

    // Getter dan setter untuk jenis motor
    std::string get_type_motor() {
        return type_motor;
    }

    void set_type_motor(std::string type_motor) {
        this->type_motor = type_motor;
    }

    // Getter dan setter untuk kapasitas tangki
    int get_tank_capacity() {
        return tank_capacity;
    }

    void set_tank_capacity(int tank_capacity) {
        this->tank_capacity = tank_capacity;
    }
};