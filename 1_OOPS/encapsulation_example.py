"""
Encapsulation involves restricting access to certain parts of an object and providing controlled access through methods. 
This helps in maintaining the integrity of the object's data and behavior. 
In Python, you can achieve encapsulation by using access modifiers and property methods.
"""
class Car:
   def __init__(self, name, release_year):
      self.name = name
      if isinstance(release_year, int):
         self._release_year = release_year
      else:
         raise ValueError('Release year must be an integer')

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


class ElectricCar(Car):
   def __init__(self, name, release_year, battery_capacity):
      super().__init__(name, release_year)
      self.battery_capacity = battery_capacity

   def get_car_details(self):
      return f'Car: {self.name}, Year: {self.release_year}, Capacity:{self.battery_capacity}'
   

#Car Constructor
car = Car('TATA', 2019)
try:
   car.release_year = '2020'
except ValueError as e:
   print("Error:", e)
print(car.get_car_details())
      