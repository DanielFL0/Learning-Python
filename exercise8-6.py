#8-6 City names: Write a function called city_country() that takes in the name of a city and its country.
#The function should return a string formatted like this: "Santiago, Chile".
#Call your function with at least three city-country pairs, and print the value that's returned.

def city_country(name, country):
    """Display the name of a city and its country"""
    formatted = name.title() + ", " + country.title()
    return formatted

print(city_country('stockholm', 'sweden'))
print(city_country('quebec', 'canada'))
print(city_country('ontario', 'canada'))
