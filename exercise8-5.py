#8-5 Cities: Write a function called describe_city() that accepts the name of a city and its country.
#The function should print a simple sentence, such as "Reykjavik is in Iceland".
#Give the parameter for the country a default value.
#Call your function for three different cities, at least one of which is not in the default country.

def describe_city(name, country='canada'):
    """Display the name of a city and its country"""
    print(name.title() + " is in " + country.title())

describe_city('ontario')
describe_city('quebec')
describe_city('stockholm', 'sweden')
