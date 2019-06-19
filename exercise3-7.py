#3-7 Shrinking guest list: You just found out that your new dinner table won't arrive in time fot the dinner, and you have space for only two guests.
#Start with your program from exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner.
#Print a message to each of the two people still on your list, letting them know they're still invited.
#Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

guest_list = ['Samuel', 'Daniel', 'Jose']
print("Hello " + guest_list[0] + " you're invited to my dinner!")
print("Hello " + guest_list[1] + " you're invited to my dinner!")
print("Hello " + guest_list[2] + " you're invited to my dinner!")

print(guest_list[1] + " isn't able to come to the dinner")
guest_list[1] = 'Sergio'

print("Hello " + guest_list[0] + " you're invited to my dinner!")
print("Hello " + guest_list[1] + " you're invited to my dinner!")
print("Hello " + guest_list[2] + " you're invited to my dinner!")

print("I've found a larger dinner table, which means I can invite more people!")

guest_list.insert(0, 'Diego')

guest_list.insert(2, 'Ernesto')

guest_list.append('Luis')

print("Hello " + guest_list[0] + " you're invited to my dinner!")
print("Hello " + guest_list[1] + " you're invited to my dinner!")
print("Hello " + guest_list[2] + " you're invited to my dinner!")
print("Hello " + guest_list[3] + " you're invited to my dinner!")
print("Hello " + guest_list[4] + " you're invited to my dinner!")
print("Hello " + guest_list[5] + " you're invited to my dinner!")

print("I'm sorry, the bigger dinner table ins't available, which means I can only invite 2 persons")

uninvited_guest = guest_list.pop()
print("Hello " + uninvited_guest + " the dinner is cancelled")
uninvited_guest = guest_list.pop()
print("Hello " + uninvited_guest + " the dinner is cancelled")
uninvited_guest = guest_list.pop()
print("Hello " + uninvited_guest + " the dinner is cancelled")
uninvited_guest = guest_list.pop()
print("Hello " + uninvited_guest + " the dinner is cancelled")

print("Hello " + guest_list[0] + " you're invited to my dinner!")
print("Hello " + guest_list[1] + " you're invited to my dinner!")

del guest_list[1]
del guest_list[0]

print(guest_list)
