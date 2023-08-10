# Hierarchical Inheritance Example
# Hierarchical inheritance allows you to create multiple subclasses that share a common superclass, but each subclass can have its own unique behavior or attributes.

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


class SUV(Vehicle):
   def __init__(self, make, model, capacity):
      super().__init__(make, model)
      self.capacity = capacity

   def get_info(self):
      return f"SUV: {self.make} {self.model}, Capacity: {self.capacity}"

# Usage
car = Car('Toyota', 'Corolla', 4)
suv = SUV('Ford', 'Explorer', 7)

print(car.get_info())
print(suv.get_info())


"""
In this example, both Car and SUV classes inherit from the Vehicle class, creating a hierarchical inheritance structure. 
Each subclass shares the common attributes and methods defined in the Vehicle class while also having their own specialized attributes and methods.
"""