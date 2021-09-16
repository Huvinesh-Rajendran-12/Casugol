class Vehicle:
    def __init__(self):
        self.make = " "
        self.model = " " 
        self.year = 0 
        self.color = " " 
        self.mileage = 0 

    def addVehicle(self):
        try: 
            self.make = input("Enter vehicle maker name: ") 
            self.model = input("Enter vehicle model :") 
            self.year = int(input("Enter vehicle year :")) 
            self.color = input("Enter vehicle color :") 
            self.mileage = int(input("Enter vehicle mileage :")) 
            return True 
        except ValueError: 
            print("Please try entering the year and mileage in integer") 
            return False
    def __str__(self):
        return ','.join(str(x) for x in [self.make,self.model,self.year,self.color,self.mileage])  


