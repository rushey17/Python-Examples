#Polymorphism allows you to write flexible and reusable code by interacting with objects through a common interface, regardless of their specific types.

class Car:
   def __init__(self, name, release_year):
      self.name = name
      self._release_year = release_year

   @property
   def release_year(self):
      return self._release_year

   @release_year.setter
   def release_year(self, year):
      if isinstance(year, int) and year >= 2000:
         self._release_year = year
      else:
         raise ValueError('Invalid Year!')

   def get_car_details(self):
      return f'Car: {self.name}, Year: {self.release_year}'

   def update_release_year(self, release_year):
      self.release_year = release_year

# Subclass ElectricCar
class ElectricCar(Car):
   def __init__(self, name, release_year, battery_capacity):
      super().__init__(name, release_year)
      self.battery_capacity = battery_capacity

   def get_car_details(self):
      return f'Electric Car: {self.name}, Year: {self.release_year}, Capacity: {self.battery_capacity}'

# Subclass LuxuryCar
class LuxuryCar(Car):
   def __init__(self, name, release_year, features):
      super().__init__(name, release_year)
      self.features = features

   def get_car_details(self):
      return f'Luxury Car: {self.name}, Year: {self.release_year}, Features: {self.features}'

# Polymorphism example
def print_car_info(car):
   print(car.get_car_details())

# Usage
car = Car('Toyota', 2020)
electric_car = ElectricCar('Tesla', 2022, 12400)
luxury_car = LuxuryCar('Mercedes', 2023, 'Leather Seats, Premium Sound')

# Using polymorphism to print details of different car types
print_car_info(car)
print_car_info(electric_car)
print_car_info(luxury_car)

"""
In this example, the print_car_info function demonstrates polymorphism by accepting objects of different subclasses (Car, ElectricCar, LuxuryCar) as its parameter 
and calling their get_car_details methods. The function treats each object as a Car object due to their shared method interface, 
and it prints out the details of each car type using the method appropriate for that subclass.
"""