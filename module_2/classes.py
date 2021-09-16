class Vehicle:
    name = "Honda" 
    kind = "car" 
    color = "black"
    value = 100000 

    def description(self):
        desc_str = "The %s  %s  %s is worth $%.2f." %(self.color,self.name,self.kind,self.value)
        return desc_str 


car = Vehicle()

print(car.description())  

 




