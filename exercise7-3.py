#7-3 Multiples of ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

prompt = "Please enter any number, and I will tell you if it's a multiple of 10 \n"
number = input(prompt)
number = int(number)

if number % 10 == 0:
    print("Your number is a multiple of 10")
else:
    print("Your number is not a multiple of 10")
