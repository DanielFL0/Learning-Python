#9-7 Admins: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in exercise9-3.py (page 166) or exercise9-5.py (page 171).
#Add an attribute privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.
#Write a method called show_privileges() that lists the administrator's set of privileges.
#Create an instance of Admin, and call your method.

#Using exercise9-5.py
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
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """A method that displays admin's privileges"""

        for privilege in self.privileges:
            print(privilege)

admin = Admin('daniel', 'saldana', 'dsal', 20)
admin.show_privileges()
