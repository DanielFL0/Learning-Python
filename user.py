#Module that contains only the User class from exercise9-8.py

class User():
    """A class that represents a user"""

    def __init__(self, first_name, last_name, user_name, age):
        """Initialize attributes to describe a user"""
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Describes user's information"""
        print("First name: "
                + self.fisrt_name.title()
                + "\nLast name: "
                + self.user_name
                + "\nAge: "
                + str(self.age)
                + "\nLogin attempts: "
                + str(self.login_attempts))

    def greet_user(self):
        """Greets the user with a simple message and it's username"""
        print("Hello, " + self.user_name + "!\n")

    def increment_login_attempts(self):
        """Increments user's login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets user's login attempts"""
        self.login_attempts = 0
