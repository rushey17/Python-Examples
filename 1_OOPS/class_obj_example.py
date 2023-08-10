class Car:
   def __init__(self, name, release_year):
      self.name = name
      self.release_year = release_year

   def get_car_details(self):
      return f'Car: {self.name}, Year: {self.release_year}'

   def update_release_year(self, release_year):
      self.release_year = release_year

car = Car('Toyota', 2020)
car.update_release_year(2022)
result = car.get_car_details()
print(result)