#8-14 Cars: Write a function that stores information about a car in a dictionary. 
#The function should always recieve a manufacturer and a model name, it should then accept an arbitrary number of keyword arguments. 
#Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:
#car = make_car('subaru', 'outback', color='blue', tow_package=True)

def make_car(manufacturer, model, **car_info):
    """Build dictionary with any information about the car"""
    car = {}
    car['manufacturer_name'] = manufacturer
    car['model_name'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car('honda', 'civic', color='red', turbo_plus=True)
print(car)
