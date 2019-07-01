#7-5 Movie tickets: A movie theater charges different ticket prices depending on a person's age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
#Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

prompt = "Welcome to the movie theater! Please enter your age."
prompt += "\nTo stop the program just write 'quit'. "
while True:
    message = "The price of your movie ticket is: "
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print(message + "FREE")
        elif age < 12:
            print(message + "$10")
        else:
            print(message + "$15")
