# Icecream Shop App
#Author A.M.H

#Store our ice creams shop's menu items
flavors = ["Vanilla", "Caramel", "Mint", "Cookie Dough"]
toppings = ["sprinkles", "nuts", "cherry","strawberrys"]
prices = {"Scoop":2.50, "Toppings": 0.50 }

def display_menu ():
    """Shows avaiable flavors and toppings to the customer"""
    print("\n===welcome to the Icecream Shop! ===")
    print("\nAvailable flavors:")

    #Loop through the flavor list and show each flavor, then
    # we'll loop though the toppings list and display them
    for flavor in flavors:
        print(f" - {flavor}")

    print("\nAvailable Toppings:")
    for topping in toppings:
        print(f"- {topping}") 

    #Display Prices
    print("\nPrices")
    print(f"Scoops: ${prices['Scoop']:.2f} each") 
    #2f means t digits the the left of the float(Price)
    print(f"Toppings: ${prices['Toppings']:.2f} each")


def get_flavors():
    """Gets ice cream flavor choices from the customer"""
    chosen_flavors = []
    #Use while loop go keep taking orders until the customer is done
    while True:
        try:
            #Prompt user to choose theri scoops of ice cream
            num_scoops = int(input("\n how many scoops would you like? (1-4)"))#input always comes as a string
            if 1 <= num_scoops <=4:
                break
            print("Please choose between 1-4 scoops.")
        except ValueError:
            print("Please enter a number.")
    
    #Prompt the user to enter an ice cream flavor
    print("\nFor each scoop, enter the flavor you'd like:")
    for i in range(num_scoops):# For loop prompts for each scoop of the ice cream
        #nested while loop handles user input and validation
        while True:
            flavors = input(f"Scoop {i+1}: ").lower()
            #check to see if their chosen flavor is on the list
            if flavors in flavors:
                chosen_flavors.append(flavors)
                break
            print("Sorry, that flavor isn't available.")

    #return to the calling function, the number of scoops the user wants
    return num_scoops, chosen_flavors
    #and the flavors they picked
def get_toppings():
    #Gets topping choices from the customer
    chosen_toppings = []
    #use while loop to prompt user for their toppings until they are done
    #choosing 
    while True:
        topping = input("\nEnter a topping( sprinkles, nuts, cherrys, strawberrys or done if finished): ").lower()
        if topping == "done":
            break
        #test if toppings are in shop
        if topping in toppings:
            chosen_toppings.append(topping)
            print(f"added topping")
        else:
            print("Sorry that topping isn't available.")
    
    return chosen_toppings

def calculate_total(num_scoops, num_toppings):
    """Calculates the total cost of the order"""
    scoop_cost = num_scoops * prices["Scoop"]
    toppings_cost = num_toppings * prices["Toppings"]
    return scoop_cost + toppings_cost

def print_receipt(num_scoops, chosen_flavors, chosen_toppings):
    print("\n=== Your Ice cream order ===")
    for i in range(num_scoops):
        print(f"Scoop {i+1}: {chosen_flavors[i].title()}")
                    #Makes it code start counting at 1
    if chosen_toppings:
        print("\nToppings:")
        #loop through the tops
        for toppings in chosen_toppings:
            print(f" - {toppings.title()}")
    #print the total
    total = calculate_total(num_scoops, len(chosen_toppings))
    print(f"\nTotal: ${total:.2f}")
    #save order to file
    with open("daily_orders.txt", "a") as file:
        file.write(f"/nOrder: {num_scoops} scoops -${total:.2f}")


#Main function - simple test function
def main():
    display_menu()
    #calls get flavor functipn, which retruns # of scoops
    #and the list of flavors
    num_scoops, chosen_flavors = get_flavors()
    chosen_toppings= get_toppings()
#display recipt
    print_receipt(num_scoops, chosen_flavors, chosen_toppings)

#Automatically executes the main function when the app runs
if __name__ == "__main__":
    main()