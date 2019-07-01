#7-9 No pastrami: Using the list sandwich_orders form exercise7-8.py, make sure the sandwich 'pastrami' appears in the list at least three times.
#Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
#Make sure no pastrami sandwiches end up in finished sandwiches.

#Using exercise7-8.py
print("Sorry! Pastrami sandwiches aren't available.")
sandwich_orders = ['tuna', 'pastrami', 'pizza', 'cheese', 'pastrami', 'cheese', 'tuna', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("Currently making " + current_sandwich + " sandwich")
    finished_sandwiches.append(current_sandwich)

print("The following sandwiches were made: ")
for sandwich in finished_sandwiches:
    print(sandwich)
