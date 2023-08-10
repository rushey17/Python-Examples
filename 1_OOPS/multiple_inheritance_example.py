# Multiple Inheritance Example
# In multiple inheritance, a class inherits from multiple classes. This can lead to inheriting attributes and methods from multiple sources.

class Engine:
   def start(self):
      return "Engine started"


class ElectricMotor:
   def start(self):
      return "Electric motor started"


class HybridCar(Engine, ElectricMotor):
   def start(self):
      engine_start = super(Engine, self).start()  # access Parent class attributes
      motor_start = super(ElectricMotor, self).start()
      return f"Hybrid car started: {engine_start}, {motor_start}"

# Usage
hybrid_car = HybridCar()
print(hybrid_car.start())


"""
In this example, HybridCar inherits from both Engine and ElectricMotor, creating a multiple inheritance scenario. 
The start method in HybridCar resolves conflicts between the two parent classes by using super() to call 
the appropriate methods from both parent classes.
"""