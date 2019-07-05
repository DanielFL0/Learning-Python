#9-4 Number served: Start with your program from exercise9-1.py (page 166).
#Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. 
#Print the number of costumers the restaurant has served, and then change this value and print it again.
#Add a method called set_number_served() that lets you set the number of costumers that have been served. 
#Call this method with a new number and print the value again.
#Add a method called increment_number_served() that lets you increment the number of costumers who've been served.
#Call this method with any number you like that could represent how many customers were served in, say, a day of business.

#Using exercise9-1.py
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

restaurant = Restaurant('subway', 'sandiwch restaurant')
print(restaurant.number_served)
restaurant.number_served = 21
print(restaurant.number_served)
restaurant.set_number_served(45)
print(restaurant.number_served)
restaurant.increment_number_served(100)
restaurant.describe_restaurant()
