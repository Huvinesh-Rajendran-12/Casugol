import os 
import vehicle as V  
class Inventory:
    def __init__(self):
        self.vehicles = []  
    def addVehicle(self):
        vehicle1 = V.Vehicle() 
        if vehicle1.addVehicle() == True:
            self.vehicles.append(vehicle1) 
            print() 
            print("The vehicle has been added") 
    def viewInventory(self):
        print(','.join(['id','Make','Model','Year','Color','Mileage']))    
        for index,vehicle in enumerate(self.vehicles):
            print(str(index+1),end=',')
            print(vehicle) 

        

def main():
    inventory = Inventory() 
    err_count = 0
    line_counter = 0
    while True:
        print(""" 
                1. Add vehicle to inventory
                2. Delete vehicle from inventory
                3. View current inventory 
                4. Update vehicle in inventory 
                5. Save the records to file 
                6. Quit 
                """) 
        choice = input("Enter the option :") 

        if choice in ['1','2','3','4','5','6']:
            if choice == '1':
                inventory.addVehicle() 
            elif choice == '2':
                if len(inventory.vehicles) < 1:
                    print("There are no vehicles in the inventory") 
                    continue
                else :
                    inventory.viewInventory()
                    id = int(input("Enter the number of vehicle that needs to be removed :"))
                    if id-1 > len(inventory.vehicles):
                        print("This is an invalid input...") 
                    else:
                        inventory.vehicles.remove(inventory.vehicles[id-1]) 
                        print("Vehicle removed") 
                        continue 
            elif choice == '3':
                if len(inventory.vehicles) < 1:
                    print("There are no vehicles in the inventory") 
                    continue 
                inventory.viewInventory() 

            elif choice == '4': 
                if len(inventory.vehicles ) < 1: 
                    print("There are no vehicles in the inventory") 
                    continue 
                inventory.viewInventory() 
                id = int(input("Enter the id of the vehicle wish to be updated :")) 
                if id-1 > len(inventory.vehicles):
                    print("This is an invalid number")  
                else :
                    vehicle2 = V.Vehicle() 
                    if vehicle2.addVehicle() == True:
                        inventory.vehicles.remove(inventory.vehicles[id-1]) 
                        inventory.vehicles.insert(id-1,vehicle2)
                        print() 
                        print(" This vehicle has been updated")

            elif choice == '5':
                if os.path.isfile('car_inventory.txt') == True:
                    f = open('car_inventory.txt','r+') 
                    linecount = len(f.readlines()) 
                    for index,vehicle in enumerate(inventory.vehicles):
                        index = index + linecount 
                        f.write("%d,%s\n" %(index,vehicle)) 
                else:
                    f = open('car_inventory.txt','w+')
                    linecount = len(f.readlines()) 
                    f.write(','.join(['id','Maker''Model','Year','Color','Mileage']))
                    f.write('\n') 
                    for index,vehicle in enumerate(inventory.vehicles):
                        index = index + linecount + 1
                        f.write("%d,%s\n" %(index,vehicle)) 
                f.close()        
                print("Saved to file")    
            else :
                print("Exiting the program...") 
                break

        else:
            if err_count == 0 :
                err_count += 1 
                print("Warning : Wrong option entered... count 1")
            elif err_count == 1:
                err_count += 1 
                print("Warning : Second wrong option.. third time will quit the programe") 
            else :
                print("Quitting the program...") 
                break 


if __name__ == "__main__":
    main() 





