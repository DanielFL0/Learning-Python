#8-10 Great magicians: Start with a copy of your program from exercise8-9.
#Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician's name.
#Call show_magicians() to see that the list has actually been modified.

def make_great(magicians):
    """Add the Great to each magician's name"""
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        magician += " the Great"
        great_magicians.append(magician)
    return great_magicians

def show_magicians(magicians):
    """Display a list of magicians"""
    for magician in magicians:
        print(magician.title())

magicians = ['houdini', 'penn', 'teller']
magicians = make_great(magicians)
show_magicians(magicians)
