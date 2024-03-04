#include <iostream>
#include <string>

#ifndef Vehicle_H
#define Vehicle_H

class Vehicle {
private:
    std::string plate_number;
    std::string brand;
    int year;
    std::string color;

public:
    // Konstruktor untuk kelas Vehicle
    Vehicle(std::string plate_number, std::string brand, int year, std::string color)
        : plate_number(plate_number), brand(brand), year(year), color(color) {}

    // Getter dan setter untuk plat nomor
    std::string get_plate_number() const{
        return plate_number;
    }

    void set_plate_number(std::string plate_number) {
        this->plate_number = plate_number;
    }

    // Getter dan setter untuk merk
    std::string get_brand() const{
        return brand;
    }

    void set_brand(std::string brand) {
        this->brand = brand;
    }

    // Getter dan setter untuk tahun produksi
    int get_year() const{
        return year;
    }

    void set_year(int year) {
        this->year = year;
    }

    // Getter dan setter untuk warna
    std::string get_color() const{
        return color;
    }

    void set_color(std::string color) {
        this->color = color;
    }

};
#endif // VEHICLE_H