#3-9 Dinner guests: Working with one of the programs from exercises 3-4 through 3-7 (page 46), use len() to print a message indicating the number of people you are inviting to dinner.

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

#Printing length of guest_list to find out how many people are invited to my dinner.
print("The total number of guests is: " + str(len(guest_list)))
