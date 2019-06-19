#3-5 Changing guest list: You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll have to think of someone else to invite.
#Start with your program from exercise 3-4. Add a print statement at the end of your program stating the name of the guest who can't make it.
#Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.
#Print a second set of invitation messages, one for each person who is still in your list.

guest_list = ['Samuel', 'Daniel', 'Jose']
print("Hello " + guest_list[0] + " you're invited to my dinner!")
print("Hello " + guest_list[1] + " you're invited to my dinner!")
print("Hello " + guest_list[2] + " you're invited to my dinner!")

print(guest_list[1] + " isn't able to come to the dinner")
guest_list[1] = 'Sergio'

print("Hello " + guest_list[0] + " you're invited to my dinner!")
print("Hello " + guest_list[1] + " you're invited to my dinner!")
print("Hello " + guest_list[2] + " you're invited to my dinner!")

