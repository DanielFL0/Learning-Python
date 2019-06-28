#6-1 Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live.
#You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

person = {
    'first_name': 'daniel',
    'last_name': 'saldaña flores',
    'age': 20,
    'city': 'Monterrey'
    }
print("My first name is " + person['first_name'])
print("My last name is " + person['last_name'])
print("My age is " + str(person['age']))
print("The city where I live is " + person['city'])
