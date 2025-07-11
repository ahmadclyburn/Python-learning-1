from model.Car import Car 
import time
class VehicleImplementation:
  def __init__(self, cars):
        self.cars = {car.vehicleId: car for car in cars} 
  @staticmethod
  def typewriter_print_fast(text, delay=0.000005):
          """Simulates typing effect for the given text."""
          for char in text:
              print(char, end='', flush=True)
              time.sleep(delay)
          print()
  def typewriter_print_slow(text, delay=0.005):
          """Simulates typing effect for the given text."""
          for char in text:
              print(char, end='', flush=True)
              time.sleep(delay)
          print()      

  def listAll(self):
    if not self.cars:
        self.typewriter_print_slow("No cars in inventory.")
        return
    self.typewriter_print_slow("All Cars:")
    for car in self.cars.values():
        self.typewriter_print_fast(
            f"{car.get_make()}, {car.get_model()}, {car.get_color()}, {car.get_odometerReading()}, {car.get_price()}"
        )
    return self.cars
  
  def add(self):
    input("please enter the following details:")
    vehicleId = input("vehicleId: ")
    make = input("make: ")
    model = input("model: ")
    color = input("color: ")
    odometerReading = input("odometerReading: ")
    price = input("price: ")
    new_car = Car(vehicleId, make, model, color, odometerReading, price)
    pass
  
  def delete(self):
      vehicleId = input("Enter the vehicleId of the car to delete: ")
      if vehicleId in self.cars:
        del self.cars[vehicleId]
        self.typewriter_print_slow(f"Car with vehicleId {vehicleId} has been deleted.")
      else:
          self.typewriter_print_slow(f"Car with vehicleId {vehicleId} not found.")
          pass
      
  def update(self):
      vehicleId = input("please enter the vehicle id of the car you want to update: ")
      self.typewriter_print_slow ("If you dont want to update a field, just enter its present info.")
      if vehicleId in self.cars:
          make = input("enter new make: ")
          model= input("enter new make and model:")
          color = input("enter new color: ")
          odometerReading = input("enter new odometer reading: ")
          price = input("enter new price: ")
          car = self.cars[vehicleId]
          self.typewriter_print_slow(f"Updating car with vehicleId {vehicleId}...")
          time.sleep(2)
          self.typewriter_print_slow(f"details have been updated to:{make}, {model}, {color}, {odometerReading}, {price}")
      else: 
          self.typewriter_print_slow(f"Car with vehicleId {vehicleId} not found.")
          pass
      
  def find(self):
      vehicleId = input("enter the vehicleId of the car you want to find: ")
      if vehicleId in self.cars:
          car = self.cars[vehicleId]
          self.typewriter_print_fast(f"Car found: {car.get_make()}, {car.get_model()}, {car.get_color()}, {car.get_odometerReading()}, {car.get_price()}")
      else:
          self.typewriter_print_slow(f"Car with vehicleId {vehicleId} not found.")
          return self.cars
  