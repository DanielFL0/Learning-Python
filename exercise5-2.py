#5-2 More conditional tests: You don't have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:
#Tests for equality and inequality with strings
#Tests using the lower() function
#Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
#Tests using the and keyword and the or keyword
#Test wether an item is in a list
#Test wether an item is not in a list.

#equality with strings
name = 'Daniel'
print("Is name = 'Daniel'?")
print(name == 'Daniel')
print("Is name = 'John'?")
print(name == 'John')

#inequality with strings
print("Is name != 'Daniel'?")
print(name != 'Daniel')
print("Is name != 'John'?")
print(name != 'John')

#lower() function
print("Is name = 'daniel'?")
print(name == 'daniel')
print("Is name.lower() = 'daniel'?")
print(name.lower() == 'daniel') 

#Numerical test involving equality
favoriteNumber = 1337
print("Is your favorite number = 5?")
print(favoriteNumber == 5)
print("Is your favorite number = 1337?")
print(favoriteNumber == 1337)

#numerical test involving inequality
print("Is your favorite number != 5?")
print(favoriteNumber != 5)
print("Is your favorite number != 1337?")
print(favoriteNumber != 1337)

#greater than
print("Is your favorite number > 1000?")
print(favoriteNumber > 1000)
print("Is your favorite number > 5000?")
print(favoriteNumber > 5000)

#less than
print("Is your favorite number < 1000?")
print(favoriteNumber < 1000)
print("Is your favorite number < 5000?")
print(favoriteNumber < 5000)

#greater than or equal to
print("Is your favorite number >= 1000?")
print(favoriteNumber >= 1000)
print("Is your favorite number >= 5000?")
print(favoriteNumber >= 5000)

#less than or equal to
print("Is your favorite number <= 1000?")
print(favoriteNumber <= 1000)
print("Is your favorite number <= 5000?")
print(favoriteNumber <= 5000)

#The and keyword
value1 = 5
value2 = 9
print("Is value1 < 10 and value2 > 5?")
print(value1 < 10 and value2 > 5)
print("Is value1 < 4 and value2 > 3?")
print(value1 < 4 and value2 > 3)

#The or keyword
print("Is value1 < 10 or value2 > 12?")
print(value1 < 10 or value2 > 12)
print("Is value1 > 10 or value2 < 4?")
print(value1 > 10 or value2 < 4)

#Item is in list
foods = ['pizza', 'sandwich', 'hamburger']
print("Is 'pizza' in " + str(foods) + "?")
print('pizza' in foods)
print("Is 'ice cream' in " + str(foods) + "?")
print('ice cream' in foods)

#Item is not in list
print("Is 'cake' not in " + str(foods) + "?")
print('cake' not in foods)
print("Is 'pizza' not in " + str(foods) + "?")
print('pizza' not in foods)
