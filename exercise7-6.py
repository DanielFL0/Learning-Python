#7-6 Three exits: Write different versions of either exercise7-4 or exercise7-5 that do each of the following at least once.
#Use a conditional text in the while statement to stop the loop.
#Use an active variable to control how long the loop runs.
#Use a break statement to exit the loop when the user enters a 'quit' value.

#Using exercise7-5.py with conditional text in while statement to stop the loop.
prompt = "Welcome to the movie theater! Please enter your age."
prompt += "\nTo stop the program just write 'quit'. "
message = "The price of your movie ticket is: "
user_input = ''
while user_input != 'quit':
    user_input = input(prompt)
    if user_input != 'quit':
        if int(user_input) < 3:
            print(message + "FREE")
        elif int(user_input) < 12:
            print(message + "$10")
        elif int(user_input) >= 12:
            print(message + "$15")

#Using an active variable
active = True
while active:
    user_input = input(prompt)
    if user_input == 'quit':
        active = False
    else:
        age = int(user_input)
        if age < 3:
            print(message + "FREE")
        elif age < 12:
            print(message + "$10")
        else:
            print(message + "$15")

#Using a break statement:
while True:
    user_input = input(prompt)
    if user_input == 'quit':
        break
    else:
        age = int(user_input)
        if age < 3:
            print(message + "FREE")
        elif age < 12:
            print(message + "$10")
        else:
            print(message + "$15")
