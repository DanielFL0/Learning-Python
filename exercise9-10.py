#9-10 Imported restaurant: Using your latest Restaurant class, store it in a module.
#Make a separate file that imports Restaurant.
#Make a Restaurant instance, and call one of Restaurant's methods to show that the import statement is working properly.

#Using exercise9-6.py (Restaurant class)
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
       self.number.served = number_served

   def increment_number_served(self, number):
       """Increment the number served to a given value"""
       self.number_served += number

class IceCreamShop(Restaurant):
    """A class that represents an ice cream shop"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of class Restaurant
        And adding the attribute flavores
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']

    def show_flavors(self):
       """A simple method that displays the list of flavors"""
       for flavor in self.flavors:
           print(flavor)
