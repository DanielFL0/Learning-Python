#7-4 Pizza toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
#As they enter each topping, print a message saying you'll add that topping to their pizza.

prompt = "Welcome to Daniel's pizza! Which toppings would you like on your pizza?"
prompt += "\nWhen you're finished, just type 'quit' to finish the program. "
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print("Added " + message + " to your pizza,")
