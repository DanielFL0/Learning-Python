#Module that contains the Privileges class from exercise9-8.py

class Privileges():
    """A class that represents admin's preivileges"""

    def __init__(self):
        """Initialize attributes to describe admin's privileges"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """A method that displays admin's privileges"""

        for privilege in self.privileges:
            print(privilege)
