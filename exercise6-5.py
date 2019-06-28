#6-5 Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
#Use a loop to print a sentence about each river, such as "The Nile Runs through Egypt."
#Use a loop to print the name of each river included in the dictionary.
#Use a loop to print the name of each country included in the dictionary.

rivers = {
        'nile': 'egypt',
        'amazon river': 'peru',
        'yangtze river': 'china'
        }
for name, country in rivers.items():
    print("The " + name.title() + " Runs through " + country.title())

for name in rivers.keys():
    print("River's name: " + name.title())

for country in rivers.values():
    print("Country: " + country.title())
