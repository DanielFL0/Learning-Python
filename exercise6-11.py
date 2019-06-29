#6-11 Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
#Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about the city.
#The keys for each city's dictionary sould be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    'san francisco': {
        'country': 'United States',
        'population': 883305,
        'fact': "The first electric TV was invented in San Francisco in 1972 by Philio Farnsworth."
        },
    'boston': {
        'country': 'United States',
        'population': 694583,
        'fact': "Boston built america's first subway in 1897"
        },
    'houston': {
        'country': 'United States',
        'population': 2325502,
        'fact': "Houston is the fourth most populous city in the nation"
        }
    }

for city, information in cities.items():
    print("\n" + city.title())
    for data, facts in information.items():
        if data == 'population':
            print(data.title() + ": " + str(facts))
        else:
            print(data.title() + ": " + facts)
