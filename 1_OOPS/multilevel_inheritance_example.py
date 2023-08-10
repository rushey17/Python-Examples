# Multilevel Inheritance Example
# In multilevel inheritance, a class inherits from a class that inherits from another class. This creates a chain of inheritance.


class Vehicle:
   def __init__(self, make, model):
      self.make = make
      self.model = model

   def get_info(self):
      return f"Vehicle: {self.make} {self.model}"


class Car(Vehicle):
   def __init__(self, make, model, num_doors):
      super().__init__(make, model)
      self.num_doors = num_doors

   def get_info(self):
      return f"Car: {self.make} {self.model}, Doors: {self.num_doors}"


class ElectricCar(Car):
   def __init__(self, make, model, num_doors, battery_capacity):
      super().__init__(make, model, num_doors)
      self.battery_capacity = battery_capacity

   def get_info(self):
      return f"Electric Car: {self.make} {self.model}, Doors: {self.num_doors}, Battery: {self.battery_capacity}"

# Usage
electric_car = ElectricCar('Tesla', 'Model S', 4, '100 kWh')
print(electric_car.get_info())


"""
In this example, ElectricCar inherits from Car, 
which itself inherits from Vehicle. This creates a multilevel inheritance hierarchy.
"""