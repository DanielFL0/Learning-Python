#7-10 Dream vacation: Write a program that polls users about their dream vacation.
#Write a prompt similar to "If you could visit one place in the world, where would you go?"
#Include a block of code that print the results of the poll.

vacation_places = {}
prompt = "If you could visit one place in the world, "
prompt += "where would you go? "

active = True
while active:
    name = input("Please enter your name: ")
    vacation_places[name] = input(prompt)
    answer = input("Would you like to keep answering the poll? \ntype no if you want to quit. ")
    if answer.lower() == 'no':
        active = False

for name, place in vacation_places.items():
    print(name + ": " + place)

