#6-12 Extensions: We're now working with examples that are complex enough that they can be extended in any number of ways.
#Use one of the example programs from this chapter, and extend it by adding new keys and values, changing the context of the program or improving the formatting of the output.

#Using many_users.py (page 113)
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
        },
    #Adding more users
    'ntesla': {
        'first': 'nikola',
        'last': 'tesla',
        'location': 'croatia'
        },
    'aturing': {
        'first': 'alan',
        'last': 'turing',
        'location': 'united kingdom'
        }
    }

for user, information in users.items():
    print("\n" + user.title())
    for data, values in information.items():
        print(data.title() + ": " + values.title())
