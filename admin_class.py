#Module that stores the Admin class from exercise9-8.py

from user import User
from privileges import Privileges

class Admin(User):
    """A class that represents an admin"""

    def __init__(self, first_name, last_name, user_name, age):
        """
        Initialize user's attributes
        And added attribute privileges
        """
        super().__init__( first_name, last_name, user_name, age)
        self.privileges = Privileges()
