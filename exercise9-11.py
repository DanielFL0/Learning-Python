#9-11 Imported admin: Start with your work from exercise9-8 (page 178).
#Store the classes User, Privileges, and Admin in one module.
#Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

from admin import User
from admin import Admin
from admin import Privileges

page_admin = Admin('daniel', 'saldana', 'dsal', 20)
page_admin.privileges.show_privileges()
