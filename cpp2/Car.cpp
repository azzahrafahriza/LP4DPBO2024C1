#include <iostream>
#include <string>
#include <vector>
#include <bits/stdc++.h>
#include "Vehicle.cpp" // Include header file for base class

class Car : public Vehicle {
private:
    int num_seats; // Number of seats attribute
    int num_doors; // Number of doors attribute

public:
    // Constructor for Car class, inheriting attributes from Vehicle class
    Car(std::string plate_number, std::string brand, int year, std::string color, int num_seats, int num_doors) 
        : Vehicle(plate_number, brand, year, color), num_seats(num_seats), num_doors(num_doors) {}

    // Getter method for number of seats
    int get_num_seats() {
        return num_seats;
    }

    // Setter method for number of seats
    void set_num_seats(int num_seats) {
        this->num_seats = num_seats;
    }

    // Getter method for number of doors
    int get_num_doors() {
        return num_doors;
    }

    // Setter method for number of doors
    void set_num_doors(int num_doors) {
        this->num_doors = num_doors;
    }
};
