from UserInterface import UserInterface
from datamanager.DataConnector import DataConnector
from model.Car import Car
class CarApp:
    @staticmethod
    def main():
        connector = DataConnector("localhost", "root", "yearup24", "dealershipworkshop")
        connection = connector.connection
        cursor = connection.cursor()
        cursor.execute("SELECT vin, make, model, color, price, year FROM vehicles")
        cars = [Car(*row) for row in cursor.fetchall()]  # <-- Load cars from DB
        ui = UserInterface(cars)
        result = ui.mainMenu()

if __name__ == "__main__":
      CarApp.main()
      