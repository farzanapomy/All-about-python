class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
# Write getter and setter methods for Vehicle class.
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def set_mileage(self, mileage):
        self.mileage = mileage

    def get_mileage(self):
        return self.mileage
    def fare(self, capa):
        self.capa = capa
        return self.capa * 100


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)
Collage_bus = Bus("Collage Volvo", 14, 100)

# print("Vehicle Name:", School_bus.name, "Bus Mileage:", School_bus.mileage, "Bus Capacity:", School_bus.capacity)
# Check the type of the object school_bus
print(type(School_bus))
print(isinstance(School_bus, Bus))

print("Vehicle Name:", School_bus.name, "Bus Mileage:",
      School_bus.mileage, "Bus Capacity:", School_bus.capa)

