#9-14 Dice: The module random contains functions that generate random numbers
#in a variety of ways. The funcion randint() returns an integer in the range
#you provide. The following code returns a number between 1 and 6.
#Example:
#from random import randint
#x = randint(1, 6)
#Make a class Die with one attribute called sides, which has a default value of
#6.
#Write a method called roll_die() that prints a random number between 1 and the
#number of sides the die has. Make a 6-sided die and roll it 10 times.
#Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die():
    """A class that represents a die with n sides"""

    def __init__(self):
        self.sides = 6
    
    def roll_die(self):
        random_number = randint(1, self.sides)
        print("The die haves: " + str(self.sides))
        print("The die felt on the number: " + str(random_number))

die6 = Die()
for i in range(10):
    die6.roll_die()

die10 = Die()
die10.sides = 10
for i in range(10):
    die10.roll_die()

die20 = Die()
die20.sides = 20
for i in range(20):
    die20.roll_die()
