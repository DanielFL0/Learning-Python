#9-1 Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type.
#Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
#Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

class Restaurant():
    """A class that represents a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Displays restaurant information"""
        print("Restaurant's name: " + self.restaurant_name.title())
        print("Cuisine type: " + self.cuisine_type.title())
        
    def open_restaurant(self):
        """Displays a message that the restaurant is now open"""
        print(self.restaurant_name.title() + " is now open")


restaurant = Restaurant("danny's pizza", 'pizzeria')
restaurant.describe_restaurant()
restaurant.open_restaurant()
