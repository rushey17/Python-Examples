class Rectangle:
   def __init__(self, width, height):
      self.width = width
      self.height = height

   @classmethod
   def create_square(cls, side_length):
      return cls(side_length, side_length)

# Usage
rectangle = Rectangle(4, 6)
square = Rectangle.create_square(5)

print(f"Rectangle: {rectangle.width}x{rectangle.height}")
print(f"Square: {square.width}x{square.height}")


"""
cls: Within a class method, cls refers to the class itself, similar to how self refers to an instance of the class within instance methods.

(side_length, side_length): This is a tuple containing two elements, both representing the width and height of the rectangle. Since we want to create a square, both the width and height are set to the same value, which is the side_length.

cls(side_length, side_length): This line creates a new instance of the class Rectangle using the provided side_length value for both the width and height attributes.

In essence, the line cls(side_length, side_length) is equivalent to calling the Rectangle constructor (__init__) with the specified arguments to create a new square Rectangle object.
"""


"""
USES OF CLASS METHODS:

Class methods are useful in a variety of scenarios where you need to work with class-level attributes, perform operations related to the class as a whole, or provide alternative ways to create instances. Here are some common situations where you might use class methods:

Alternate Constructors: You can use class methods as alternative constructors to provide different ways to create instances of the class. This can be helpful when you want to initialize objects using different sets of parameters.

Factory Methods: Class methods can act as factory methods that create and return instances of the class. This is useful when you want to encapsulate the creation process and provide a clear interface for object creation.

Accessing Class-Level Attributes: Class methods can access and modify class-level attributes. This is especially useful when you want to perform operations or calculations based on these attributes.

Singleton Pattern: Class methods can be used to implement the Singleton design pattern, ensuring that only one instance of a class is created throughout the program.

Initialization Logic: If you have complex initialization logic that involves multiple steps or calculations, you can encapsulate this logic within a class method to keep the __init__ method clean.

Class Utilities: Class methods can serve as utility functions related to the class, even if they don't directly create instances. For example, they can perform data validation, transformation, or provide information about the class.

Subclassing and Inheritance: Class methods can be overridden in subclasses to provide specialized behavior. This allows subclasses to customize the behavior of class methods inherited from the parent class.

Encapsulation and Abstraction: Class methods can be used to encapsulate complex operations or algorithms that are related to the class but don't directly involve instance attributes.
"""