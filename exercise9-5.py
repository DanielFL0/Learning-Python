#9-5 Login attempts: Add an attribute called login_attempts to your User class from exercise9-3.py (page 166).
#Write a method called increment_login_attepts() that increments the value of login_attempts by 1.
#Write another method called reset_login_attempt() that resets the value of login_attempts to 0.
#Make an instance of the User class and call increment_login_attempts() several times.
#Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
#Print login_attempts again to make sure it was reset to 0.

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
                + self.first_name.title()
                + "\nLast name: "
                + self.last_name.title()
                + "\nUser name: "
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

user = User('daniel', 'saldana', 'dsal', '20')
for i in range(5):
    user.increment_login_attempts()

print("Login attempts: " + str(user.login_attempts))
user.reset_login_attempts()
print("Login attempts: " + str(user.login_attempts))
