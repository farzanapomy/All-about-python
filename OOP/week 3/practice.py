class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    # Define a property that must have the same value for every class instance (object)
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def mileage(self):
        return self.__mileage
    @mileage.setter
    def mileage(self, mileage):
        self.__mileage = mileage
        
class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print("Vehicle Name:", School_bus.name, "Mileage:", School_bus.mileage, "Capacity:", School_bus.capacity)

#  Create a class with instance attributes
College_bus = Bus("College Volvo", 18, 50)

# Check the type of the object school_bus and college_bus
print("type of school_bus:", type(School_bus))
print("type of college_bus:", type(College_bus))


# Check if School_bus is also an instance of the Vehicle class.
print(isinstance(School_bus, Vehicle))


# Define a property that must have the same value for every class instance (object)
