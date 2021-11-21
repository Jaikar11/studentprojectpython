# This is a child class of Vehicle class
from Vehicle import Vehicle


class Car(Vehicle):
    def carDetails(self, veh_type=None, car_make=None, car_colour=None, car_model=None):
        super.__init__(veh_type, car_make, car_colour, car_model)  # super calls the constructor of the parent class


print("Car class is child class of Vehicle class(Parent) ")
car1 = Car("Car", "Volvo", "Grey", "Golf");
car1.printDetails()

car4 = Car("Car", "Vauxhall", "White", "Astra");
car1.printDetails()