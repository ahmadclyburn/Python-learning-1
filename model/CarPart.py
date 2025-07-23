class CarPart:
    def __init__(self, categoryId ,partId, partName, description, manufacturer, vehicleMake, vehicleModel, yearRange, price, stockQuantity, dateAdded):
        self.categoryId = categoryId
        self.partName = partName
        self.partId = partId
        self.description = description
        self.manufacturer = manufacturer
        self.vehicleMake = vehicleMake
        self.vehicleModel = vehicleModel
        self.yearRange = yearRange
        self.price = price
        self.stockQuantity = stockQuantity
        self.dateAdded = dateAdded
    def get_partName(self):
        return self.partName
    def set_partName(self, partName):
        self.partName = partName   
    def get_partId(self):
        return self.partId
    def set_partId(self, partId):
        self.partId = partId
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price   
    def get_categoryId(self):
        return self.categoryId
    def set_categoryId(self, categoryId):
        self.categoryId = categoryId
    def get_description(self):
        return self.description
    def set_description(self, description):
        self.description = description
    def get_manufacturer(self):
        return self.manufacturer
    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer
    def get_vehicleMake(self):
        return self.vehicleMake
    def set_vehicleMake(self, vehicleMake):
        self.vehicleMake = vehicleMake
    def get_vehicleModel(self):
        return self.vehicleModel
    def set_vehicleModel(self, vehicleModel):
        self.vehicleModel = vehicleModel
    def get_yearRange(self):
        return self.yearRange
    def set_yearRange(self, yearRange):
        self.yearRange = yearRange
    def get_stockQuantity(self):
        return self.stockQuantity  
    def set_stockQuantity(self, stockQuantity):
        self.stockQuantity = stockQuantity
    def get_dateAdded(self):
        return self.dateAdded  
    def set_dateAdded(self, dateAdded):
        self.dateAdded = dateAdded