#9-6 Ice cream stand: An ice cream stand is a sepcific kind of restaurant.
#Write a class called IceCreamStand that inherits from the Restaurant class you wrote in exercise9-1.py (page 166) or exercise9-4.py (page 171).
#Either version of the class will work; just pick the one you like better.
#Add an attribute called flavors that stores a list of ice cream flavors.
#Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.

#Using exercise9-4.py
class Restaurant():
    """A class that represents a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Displays restaurant information"""
        print("Restaurant's name: " 
                + self.restaurant_name.title()
                + "\nCuisine type: "
                + self.cuisine_type.title()
                + "\nNumber served: "
                + str(self.number_served))

    def open_restaurant(self):
        """Displays a message that the restaurant is now open"""
        print(self.restaurant_name.title() + " is now open")

    def set_number_served(self, number_served):
        """Set the number served to a given value"""
        self.number_served = number_served
    
    def increment_number_served(self, number):
        """Increment the number served to a given value"""
        self.number_served += number

class IceCreamShop(Restaurant):
    """A class that represents an ice cream shop"""
    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of class Restaurant
        And adding the attribute flavors
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def show_flavors(self):
        """A simple method that displays the list of flavors"""
        for flavor in self.flavors:
            print(flavor)

iceCreamShop = IceCreamShop("danny's ice cream", "ice cream")
iceCreamShop.show_flavors()
