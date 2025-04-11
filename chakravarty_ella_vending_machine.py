"""
Vending Machine
Ella Chakravarty

Program simulates a vending machine with soda, coffee, and water.
Allows user to purchase, restock, and check inventory. 

"""
#Define vending machine class and parameters
class vending_machine:
    def __init__(self, soda = 10, coffee = 10, water = 10):
        self.inventory = { #Specify drink IDs to initialize inventory
            1: {"name": "Soda", "count": soda},
            2: {"name": "Coffee", "count": coffee},
            3:{"name": "Water", "count": water},
        } 
    def purchase(self,choice): #Method to purchase a drink
        drink = self.inventory.get(choice) #Gets drink by number
        if drink:
            if drink ["count"] > 0: #Only allows purchase if in stock
                drink["count"] -= 1 #If drink purchased, updates inventory
                print("Dispensing...")
            else:
                print("Out of stock.")
        else:
            print("Invalid entry.")
    def restock(self, choice, amount): #method to restock a selected drink
        drink = self.inventory.get(choice)
        if drink:
            drink ["count"] += amount #add amount given to choice selected and store in inventory
            print(f"Restocked {amount} bottles of {self.inventory[choice]['name']}.")
        else:
            print("Invalid entry.")
    def report(self): #method to report current inventory
        print("Inventory")
        for drink in self.inventory.values(): #loop over each drink
            print(f"{drink['name']}: {drink['count']} bottles")

#create main program to interact with the user and prcoess input
def main():
    machine = vending_machine() #create an instance of vending_machine class
    while True:
        command = input(":>").lower() #maintain case insensitivity for each method
        if command == "quit" or  command == "q": #terminates based on stop words
            print("Process finished with exit code 0")
            break
        elif command == "buy": #processes input for purchase method
            print("Please select an option:")
            print("1 - Soda")
            print("2 - Coffee")
            print("3 - Water")
            selection = input(":>") #takes input to select a product
            if selection.isdigit(): #check if input is an integer
                machine.purchase(int(selection)) #calls purchase method
            else: 
                print("Invalid entry.")
        elif command == "restock": #processes input for restock method
            print("Please select an option:")
            print("1 - Soda")
            print("2 - Coffee")
            print("3 - Water")
            selection = input(":>") #Takes input to select a product
            if selection.isdigit(): #check if input is an integer
                drink_choice = int(selection)
                if drink_choice in [1,2,3]: #doesn't accept values outside of choice numbers
                    print("Please enter an amount:")
                    amount_input = input(":>") #takes input for amount to restock
                    if amount_input.isdigit(): #checks if amount input is an integer
                        amount = int(amount_input)
                        if 1 <= amount <= 100: #adds positive integers up to 100
                            machine.restock(drink_choice, amount) #restocks and updates inventory
                        else:
                            print("Please enter a valid number.")
                    else:
                            print("Please enter a valid number.")
                else:
                            print("Please enter a valid number.")
            else:
                print("Please enter a valid number.")
        elif command == "inventory": #processes input for inventory report method
            machine.report() #calls report method to print current inventory
        else:
            print("Invalid entry.")

#Start the program
if __name__ == "__main__":
    main()