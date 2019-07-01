#8-4 Large shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size='large', message='I love Python'):
    """Display shirt size and message"""
    print("T-Shirt size: " + size + "\nMessage: " + message)

#Making a large shirt with default message
make_shirt()

#Making a medium shirt with default message
make_shirt('medium')

#Making a shirt of any size with different message
make_shirt('small', 'Python is my favorite programming language!')
