#3-6 More guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
#Start with your program from exercise 3-4 or exercise 3-5. Add a print statement to the end of your program informing people that you found a bigger dinner table.
#Use insert() to add one new guest to the beginning of your list.
#Use insert() to add one new guest to the middle of your list
#Use append() to add one new guest to the end of your list.
#Print a new set of invitation messages, one for each person in your list.

guest_list = ['Samuel', 'Daniel', 'Jose']
print("Hello " + guest_list[0] + " you're invited to my dinner!")
print("Hello " + guest_list[1] + " you're invited to my dinner!")
print("Hello " + guest_list[2] + " you're invited to my dinner!")

print(guest_list[1] + " isn't able to come to the dinner")
guest_list[1] = 'Sergio'

print("Hello " + guest_list[0] + " you're invited to my dinner!")
print("Hello " + guest_list[1] + " you;re invited to my dinner!")
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
