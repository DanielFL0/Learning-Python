#7-8 Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
#Loop through the list of sandwich orders and print a message for each order, such as I made your own tuna sandwich.
#As each sandwich is made, move it to the list of finished sandwiches.
#After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['tuna', 'pizza', 'cheese']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("Currently making: " + current_sandwich.title() + " sandwich")
    finished_sandwiches.append(current_sandwich)

print("Sandwiches made: ")
for sandwich in finished_sandwiches:
    print(sandwich.title())
