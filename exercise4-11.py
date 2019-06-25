#4-11 My pizzas, your pizzas: Start with your program from exercise 4-1 (page 60). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
#Add a new pizza to the original list.
#Add a different pizza to the list friend_pizzas.
#Prove that you have two separate lists. Print the message, my favorite pizzas are;, and then use a for loop to print the first list. Print the message, My friend's favorite pizzas are;, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropiate list.

#Using exercise 4-1
pizzas = ['pepperoni', 'cheese', 'meat']
for pizza in pizzas:
    print("I like " + pizza.title() + " pizza.")

print("Pizza is my favorite food!")

friend_pizzas = pizzas[:]

pizzas.append('hawaiian')

friend_pizzas.append('chicago')

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)


