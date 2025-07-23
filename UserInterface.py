from interface_implementation.VehicleImplementation import VehicleImplementation
from interface_implementation.CarPartImplementation import CarPartImplementation
from model.Car import Car
class UserInterface:
    def __init__(self, cars, carparts):
        self.vI = VehicleImplementation(cars)
        self.cPI = CarPartImplementation(carparts)
    def mainMenu(self):     
        print("Welcome to the Car App!")
        print("This app will help you manage your car inventory.")
        input("Press Enter to continue...")
        print("1. view car menu")
        print("2. view car parts menu")
        print("3. Exit")
        choice = input("would you like to add, delete, find, or update a car?")

        match choice:
            case "1":
                self.carMenu()
            case "2":
                self.carPartsMenu()
            case "3":
                print("thank you for using the Car App. Goodbye!")
            case _:(choice, "Invalid choice. Please try again.")
    def carMenu(self):
        print("Car Menu:")
        print("1. List all cars")
        print("2. Add a car")
        print("3. Delete a car")
        print("4. Update a car")
        print("5. Find a car")
        print("6. Exit")
        choice = input("Please choose an option: ")
        
        match choice:
            case "1":
                self.vI.listAll()
            case "2":
                self.vI.add()
            case "3":
                self.vI.delete()
            case "4":
                self.vI.update()
            case "5":
                self.vI.find()
            case "6":
                self.mainMenu()
                print("Exiting the Main Menu.")
            case _:
                print("Invalid choice, please try again.")
    def carPartsMenu(self):
        print("Car Parts Menu:")
        print("1. List all car parts")
        print("2. Add a car part")
        print("3. Delete a car part")
        print("4. Update a car part")
        print("5. Find a car part")
        print("6. Go back to the main menu")
        choice = input("Please choose an option: ")
        
        match choice:
            case "1":
                self.cPI.listAll()
            case "2":
                self.cPI.add()
            case "3":
                self.cPI.delete()
            case "4":
                self.cPI.update()
            case "5":
                self.cPI.find()
            case "6":
                print("Exiting the Main Menu.")
                self.mainMenu()
            case _:
                print("Invalid choice, please try again.")