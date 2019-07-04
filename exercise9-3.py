#9-3 Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user's profile.
#Make a method called describe_user() that prints a summary of the user's information.
#Make another method called greet_user() that prints a personalized greeting to the user.
#Create several instances representing different users, and call both methods for each user.

class User():
    """A class that represents a user"""

    def __init__(self, first_name, last_name, user_name, age):
        """Initialize attributes to describe a user"""
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.age = age

    def describe_user(self):
        """Describes user's information"""
        print("First name: " 
                + self.first_name.title()
                + "\nLast name: " 
                + self.last_name.title()
                + "\nUser name: "
                + self.user_name
                + "\nAge: "
                + str(self.age)
                + "\n")


    def greet_user(self):
        """Greets the user with a simple message and it's username"""
        print("Hello, " + self.user_name + "!\n")

my_user = User('daniel', 'saldana', 'dansal', 20)
my_user.describe_user()
my_user.greet_user()
your_user = User('sergio', 'saldana', 'serchsam', 18)
your_user.describe_user()
your_user.greet_user()
