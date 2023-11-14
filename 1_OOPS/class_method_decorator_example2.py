class Circle:
   def __init__(self, radius):
      self.radius = radius
      self.calculate_area()  # Call a method to calculate area during initialization

   def calculate_area(self):
      self.area = 3.14159 * self.radius ** 2

   @classmethod
   def create_circle_with_area(cls, desired_area):
      radius = (desired_area / 3.14159) ** 0.5
      return cls(radius)  # clean initialization of radius attribute after some calculation.

# Usage
circle = Circle.create_circle_with_area(50)  # Create a circle with the desired area

print(f"Circle Radius: {circle.radius}")
print(f"Circle Area: {circle.area}")


"""
In this example, the Circle class has an __init__ method that calculates the area of the circle based on the given radius.
Additionally, there's a class method create_circle_with_area that allows you to create a circle instance based on a desired area.
"""