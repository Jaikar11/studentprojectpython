# This is a child class of Vehicle class
from Vehicle import Vehicle


class Car(Vehicle):
    def carDetails(self, veh_type=None, car_make=None, car_colour=None, car_model=None):
        super.__init__(veh_type,car_make,car_colour, car_model)


car1 = Car("Car","VW","Grey","Golf");
car1.printDetails()




