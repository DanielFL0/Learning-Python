#8-16 Imports: Using a program you wrote that has one function in it, store that function in a separate file. 
#Import the function into your main program file, and call the function using each of these approaches:
#import module_name
#from module_name import function_name
#from module_name import function_name as fn
#import module_name as mn
#from module_name import *

import build_profile
from build_profile import make_profile, show_user
from build_profile import make_profile as mp
from build_profile import show_user as su
import build_profile as bp
from build_profile import *

#using import build_profile
user = build_profile.make_profile('daniel', 'saldana', 'dsalda')
build_profile.show_user(user)


#using from build_profile import make_profile, show_user
user = make_profile('daniel', 'saldana', 'dsalda')
show_user(user)

#using from build_profile import make_profile as mp
#from build_profile import show_user as su
user = mp('daniel', 'saldana', 'dsalda')
su(user)

#using import build_profile as bp
user = bp.make_profile('daniel', 'saldana', 'dsalda')
bp.show_user(user)

#using from build_profile import *
user = make_profile('daniel', 'saldana', 'dsalda')
show_user(user)
