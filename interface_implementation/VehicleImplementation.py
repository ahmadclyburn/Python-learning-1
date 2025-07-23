from model.Car import Car 
import time
from datamanager.DataConnector import DataConnector
class VehicleImplementation:
  def __init__(self, cars):
        self.cars = {car.vehicleId: car for car in cars} 

  def listAll(self):
    if not self.cars:
        print("No cars in inventory.")
        return
    print("All Cars:")
    for car in self.cars.values():
        print(
            f"{car.get_vehicleId()}, {car.get_make()}, {car.get_model()}, {car.get_color()}, {car.get_odometerReading()}, {car.get_price()}, {car.get_year()}"
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
    year = input("year: ")
    new_car = Car(vehicleId, make, model, color, odometerReading, price, year)
    connector = DataConnector("localhost", "root", "yearup24", "dealershipworkshop")
    connection = connector.connection
    cursor = connection.cursor()
    cursor.execute(
    "INSERT INTO vehicles (vin, make, model, color, odometerReading, price, year) VALUES (%s, %s, %s, %s, %s, %s, %s)",
    (vehicleId, make, model, color, odometerReading, price, year)) 
    connection.commit()  # Commit the transaction!
    self.cars[vehicleId] = new_car  # Add to in-memory dict
    print(f"Car with vehicleId {vehicleId} has been added.")
    connection.close()
   
  
  def delete(self):
      vehicleId = input("Enter the vehicleId of the car to delete: ")
      connector = DataConnector("localhost", "root", "yearup24", "dealershipworkshop")
      connection = connector.connection
      cursor = connection.cursor()
      if cursor.rowcount > 0:
        cursor.execute("DELETE FROM vehicles WHERE vin = %s", (vehicleId,))
        print(f"Car with vehicleId {vehicleId} has been deleted.")
        if vehicleId in self.cars:
            del self.cars[vehicleId]
      else:
          print(f"Car with vehicleId {vehicleId} not found.")
          connection.close()
      
  def update(self):
      vehicleId = input("please enter the vehicle id of the car you want to update: ")
      print("If you dont want to update a field, just enter its present info.")
      if vehicleId in self.cars:
          make = input("enter new make: ")
          model= input("enter new make and model:")
          color = input("enter new color: ")
          odometerReading = input("enter new odometer reading: ")
          price = input("enter new price: ")
          year = input("enter new year: ")
          car = self.cars[vehicleId]
          connector = DataConnector("localhost", "root", "yearup24", "dealershipworkshop")
          connection = connector.connection
          cursor = connection.cursor()
          cursor.execute(
              "UPDATE vehicles SET make = %s, model = %s, color = %s, odometerReading = %s, price = %s, year =%s WHERE vin = %s ",
              (make , model, color , odometerReading , price , year, vehicleId))
      
  def find(self):
      vehicleId = input("enter the vehicleId of the car you want to find: ")
      if vehicleId in self.cars:
          car = self.cars[vehicleId]
          print(f"Car found: {car.get_make()}, {car.get_model()}, {car.get_color()}, {car.get_odometerReading()}, {car.get_price()}, {car.get_year()}")
      else:
          print(f"Car with vehicleId {vehicleId} not found.")
          return self.cars
  