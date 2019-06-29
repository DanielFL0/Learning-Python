#6-8 Pets: Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner's name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet

coby = {
    'kind': 'dog',
    'owner_name': 'thelma'
    }

chuggy = {
    'kind': 'cat',
    'owner_name': 'daniel'
    }

nesquik = {
    'kind': 'bunny',
    'owner_name': 'hannah'
    }

pets = [coby, chuggy, nesquik]

for pet in pets:
    print("Kind of animal: " + pet['kind'])
    print("Owner's name: " + pet['owner_name'])
