#8-10 Great magicians: Start with a copy of your program from exercise8-9.
#Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician's name.
#Call show_magicians() to see that the list has actually been modified.

def make_great(magician):
    """Add the Great to each magician's name"""
    magician += " the Great"
    return magician

def show_magicians(magicians):
    """Display a list of magicians"""
    for magician in magicians:
        magician = make_great(magician)
        print(magician.title())

magicians = ['houdini', 'penn', 'teller']
show_magicians(magicians)
