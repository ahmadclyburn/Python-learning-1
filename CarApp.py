from UserInterface import UserInterface
from datamanager.DataConnector import DataConnector
from model.Car import Car
from model.CarPart import CarPart
class CarApp:
    @staticmethod
    
    def main():
        connector = DataConnector("localhost", "root", "yearup24", "dealershipworkshop")
        connection = connector.connection
        cursor = connection.cursor()
        cursor.execute("SELECT vin, make, model, color, price, year, odometerReading FROM vehicles")
        cars = [Car(*row) for row in cursor.fetchall()]  # <-- Load cars from DB
        cursor.execute("SELECT category_id, part_name, part_id, description, manufacturer, vehicle_make, vehicle_model, year_range, price, stock_quantity, date_added FROM parts_inventory")
        carparts = [CarPart(*row) for row in cursor.fetchall()]  # <-- Load car parts from DB
        ui = UserInterface(cars, carparts)
        result = ui.mainMenu()

if __name__ == "__main__":
      CarApp.main()
      
      