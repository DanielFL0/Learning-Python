#6-6 Polling: Use the code in favorite_languages.py(page 104).
#Make a list of people who should take the favoirte languages poll. Include some names that are already in the dictionary and some that are not.
#Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding.
#If they have not yet taken the poll, print a message inviting them to take the poll.

#Using favorite_languages.py
favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'
        }

people = ['jen', 'phil', 'daniel', 'samuel']

for person in people:
    if person in favorite_languages.keys():
        print("Thank you " + person.title() + " for responding the poll")
    else:
        print("Hello " + person.title() + " can you respond the poll?")


