#5-5 Alien colors #3: Turn your if-else chain from exercise 5-4, into an if-elif-else chain.
#If the alien is green, print a message that the player earned 5 points.
#If the alien is yellow, print a message that the player earned 10 points.
#If the alien is red, print a message that the player earned 15 points.
#Write three versions of this program, making sure each message is printed for the appropiate color alien.

alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

