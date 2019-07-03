#8-12 Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 
#The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that is being ordered. 
#Call the function three times, using a different number of arguments each time.

def make_sandwich(*ingredients):
    """Summarize the sandwich we are going to make"""
    print("Making a sandwich with the following ingredients: ")
    for ingredient in ingredients:
        print("- " + ingredient)

#Calling the function
make_sandwich('ham', 'cheese', 'lettuce', 'tomato')
make_sandwich('cheese', 'ham', 'mustard')
make_sandwich('ham', 'bacon', 'cheese')
