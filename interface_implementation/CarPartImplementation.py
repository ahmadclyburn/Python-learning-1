import datetime
from model.CarPart import CarPart
from datamanager.DataConnector import DataConnector
class CarPartImplementation:
    def __init__(self, parts):
        self.parts = {part.partId: part for part in parts}
    
    def listAll(self):
        if not self.parts:
            print("No car parts in inventory.")
            return
        print("All Car Parts:")
        print("________________")
        for part in self.parts.values():
            print(
                f"{part.get_partId()}, {part.get_partName()}, {part.get_price()}, {part.get_stockQuantity()}"
                )
    
    def add(self):
        input("Please enter the following details:")
        partId = input("Part ID: ")
        if partId in self.parts:
            newPartId = input(f"Part with ID {partId} already exists. please enter a new Part ID: ")
            return
        partName = input("Part Name: ") 
        description = input("Description: ")
        categoryId = input("Category ID: ")
        manufacturer = input("Manufacturer: ")
        vehicleMake = input("Vehicle Make: ")
        vehicleModel = input("Vehicle Model: ")
        yearRange = input("Year Range: ")
        price = float(input("Price: "))
        stockQuantity = int(input("Stock Quantity: "))
        dateAdded = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        new_part = CarPart(categoryId, partName, partId, description, manufacturer, vehicleMake, vehicleModel, yearRange, price, stockQuantity, dateAdded)
        
        connector = DataConnector("localhost", "root", "yearup24", "dealershipworkshop")
        connection = connector.connection
        cursor = connection.cursor()
        
        if partId in self.parts:
            cursor.execute(
            "INSERT INTO parts_inventory (part_id, part_name, description, manufacturer, vehicle_make, vehicle_model, year_range, price, stock_quantity, date_added) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (newPartId, partName, description, manufacturer, vehicleMake, vehicleModel, yearRange, price, stockQuantity, dateAdded)
        )
        else: cursor.execute(
            "INSERT INTO parts_inventory (part_id, part_name, description, manufacturer, vehicle_make, vehicle_model, year_range, price, stock_quantity, date_added) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (partId, partName, description, manufacturer, vehicleMake, vehicleModel, yearRange, price, stockQuantity, dateAdded)
        )
        
        connection.commit()
        self.parts[partId] = new_part
        print(f"Car part with ID {partId} has been added.")
        connection.close()

    def delete(self):
        partId = input("Enter the Part ID of the car part to delete: ")
        connector = DataConnector("localhost", "root", "yearup24", "dealershipworkshop")
        connection = connector.connection
        cursor = connection.cursor()
        if cursor.rowcount > 0:
            cursor.execute("DELETE FROM parts_inventory WHERE part_id = %s", (partId,))
            print(f"Car part with ID {partId} has been deleted.")
            connection.commit()
            if partId in self.parts:
                del self.parts[partId]
        else:
            print(f"Car part with ID {partId} not found.")
        connection.close()

    def update(self):
        partId = input("Please enter the Part ID of the car part you want to update: ")
        if partId in self.parts:
            partName = input("Enter new Part Name (or press Enter to keep current): ")
            description = input("Enter new Description (or press Enter to keep current): ")
            manufacturer = input("Enter new Manufacturer (or press Enter to keep current): ")
            vehicleMake = input("Enter new Vehicle Make (or press Enter to keep current): ")
            vehicleModel = input("Enter new Vehicle Model (or press Enter to keep current): ")
            yearRange = input("Enter new Year Range (or press Enter to keep current): ")
            price = input("Enter new Price (or press Enter to keep current): ")
            stockQuantity = input("Enter new Stock Quantity (or press Enter to keep current): ")
            dateAdded = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            part = self.parts[partId]
            connector = DataConnector("localhost", "root", "yearup24", "dealershipworkshop")
            connection = connector.connection
            cursor = connection.cursor()

            cursor.execute(
                "UPDATE parts_inventory SET part_name = %s, description = %s, manufacturer = %s, vehicle_make = %s, vehicle_model = %s, year_range = %s, price = %s, stock_quantity = %s, date_added = %s WHERE part_id = %s",
                (
                    partName or part.get_part_name(),
                    description or part.get_description(),
                    manufacturer or part.get_manufacturer(),
                    vehicleMake or part.get_vehicle_make(),
                    vehicleModel or part.get_vehicle_model(),
                    yearRange or part.get_year_range(),
                    price or part.get_price(),
                    stockQuantity or part.get_stock_quantity(),
                    dateAdded or part.get_date_added(),
                    partId
                )
            )
            
            connection.commit()
            print(f"Car part with ID {partId} has been updated.")
            connection.close()
        else:
            print(f"Car part with ID {partId} not found.")

    def find(self, partId):
        if partId in self.parts:
            return self.parts[partId]
        else:
            print(f"Car part with ID {partId} not found.")
            return None