#9-8 Privileges: Write a separate Privileges class.
#The class should have one attribute, privileges, that stores a list of strings as described in exercise9-7.py
#Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the admin class.
#Create a new instance of admin and use your method to show its privileges.

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

class Admin(User):
    """A class that represents an admin"""

    def __init__(self, first_name, last_name, user_name, age):
        """
        Initialize user's attributes
        And added attribute privileges
        """
        super().__init__( first_name, last_name, user_name, age)
        self.privileges = Privileges()

class Privileges():
    """A class that represents admin's preivileges"""

    def __init__(self):
        """Initialize attributes to describe admin's privileges"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """A method that displays admin's privileges"""

        for privilege in self.privileges:
            print(privilege)

admin = Admin('danny', 'saldana', 'dsal', 20)
admin.privileges.show_privileges()
