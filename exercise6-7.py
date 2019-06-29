#6-7 People: Start with the program you wrote for exercise6-1 (page 102) Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
#Loop through your list of people. As you loop through the list, print everything you know about each person.

person1 = {
    'first_name': 'daniel',
    'last_name': 'saldana flores',
    'age': 20,
    'city': 'Monterrey'
    }
person2 = {
    'first_name': 'samuel',
    'last_name': 'saldana flores',
    'age': 18,
    'city': 'Monterrey'
    }
person3 = {
    'first_name': 'hannah',
    'last_name': 'saldana flores',
    'age': 14,
    'city': 'Monterrey'
    }
people = [person1, person2, person3]
for person in people:
    print("First name: " + person['first_name'])
    print("Last name: " + person['last_name'])
    print("Age: " + str(person['age']))
    print("City: " + person['city'])

