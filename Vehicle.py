# This is a parent class  - Vehicle class

class Vehicle:
    def __init__(self, v_type, make, color, model):
        self.make = make
        self.color = color
        self.model = model
        self.v_type = v_type

    def printDetails(self):
        if self.v_type == "Car":
            print("Vehicle Type:", self.v_type )
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)