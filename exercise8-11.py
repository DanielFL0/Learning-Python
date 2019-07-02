#8-11 Unchanged magicians: Start with your work from exercise8-10. Call the function make_great() with a copy of the list of magician's names. 
#Because the original list will be unchanged, return the new list and store it in a separate list.
#Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician's name

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
new_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(new_magicians)


