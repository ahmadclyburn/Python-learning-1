from interface_implementation.VehicleImplementation import VehicleImplementation
from model.Car import Car
class UserInterface:
    def __init__(self, cars):
        self.vI = VehicleImplementation(cars)

    def mainMenu(self):     
        print("Welcome to the Car App!")
        print("This app will help you manage your car inventory.")
        input("Press Enter to continue...")
        print("1. Add a car")
        print("2. Delete a car")        
        print("3. Update a car")
        print("4. find a car")
        print("5. list all cars")
        print("6. Exit")
        choice = input("would you like to add, delete, find, or update a car?")

        match choice:
            case "1":
                self.vI.add()
            case "2":
                self.vI.delete()
            case "3":
                self.vI.update()
            case "4":
                self.vI.find()
            case "5":
                self.vI.listAll()
            case "6": 
                print("thank you for using the Car App. Goodbye!")
            case _:(choice, "Invalid choice. Please try again.")