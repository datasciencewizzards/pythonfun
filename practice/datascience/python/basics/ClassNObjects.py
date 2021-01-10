# Class

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def print(self):
        print("Car has make {} and model {}".format(bmw.make, bmw.model))


bmw = Car("x1", 2020)

print("Car has make {} and model {}".format(bmw.make, bmw.model))

bmw.print()

# Modifying properties of an object
bmw = Car("x1", 2020)
bmw.make = "Mercedes Benz"
bmw.model = "2021"
bmw.print()

# Delete object property
bmw = Car("x1", 2020)
del bmw.make
# Should throw an error , no make
# bmw.print()

# Delete object property
bmw = Car("x1", 2020)
del bmw
# Should throw an error , no object bmw
# bmw.print()



