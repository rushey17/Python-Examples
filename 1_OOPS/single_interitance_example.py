class Car:
   def __init__(self, name, release_year):
      self.name = name
      self.release_year = release_year

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

car = Car('Toyota', 2020)
car.update_release_year(2022)
result = car.get_car_details()
print(result)

# Electric car constructor
electric_car = ElectricCar('Tesla', 2022, 12400)
electric_car.update_release_year(2023)  #we are overriding the parent class method
details = electric_car.get_car_details()
print(details)
print(electric_car.release_year)