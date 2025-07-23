class Car:    
    def __init__(self, vehicleId, make, model, color, price, year, odometerReading):
        self.vehicleId = vehicleId
        self.make = make
        self.model = model
        self.color = color
        self.price = price
        self.year = year
        self.odometerReading = odometerReading
    def get_vehicleId(self):
        return self.vehicleId
    def set_vehicleId(self, vehicleId):
        self.vehicleId = vehicleId
    def get_make(self):
        return self.make
    def set_make(self, make):
        self.make = make 
    def get_model(self):
        return self.model
    def set_model(self, model):
        self.model = model 
    def get_color(self):
        return self.color   
    def set_color(self, color):
        self.color = color  
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
    def get_year(self):
        return self.year
    def set_year(self, year):
        self.year = year
    def get_odometerReading(self):
        return self.odometerReading
    def set_odometerReading(self, odometerReading):
        self.odometerReading = odometerReading
    
    
    
        