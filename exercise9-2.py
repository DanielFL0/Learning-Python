#9-2 Three restaurants: Start with your class from exercise9-1.py.
#Create three different instances from the class, and call describe_restaurant() for each instance.

class Restaurant():
    """A class that represents a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes that describe a car"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Displays restaurant information"""
        print("Restaurant's name: " + self.restaurant_name.title())
        print("Cuisine type: " + self.cuisine_type.title())

    def open_restaurant(self):
        """Displays a message that the restaurant is now open"""
        print(self.restaurant_name.title() + " is now open")

pizza_restaurant = Restaurant('dannys pizza', 'pizzeria')
sandwich_restaurant = Restaurant('subway', 'sandwich')
italian_restaurant = Restaurant('pasta and more', 'italian food')

pizza_restaurant.describe_restaurant()
sandwich_restaurant.describe_restaurant()
italian_restaurant.describe_restaurant()
