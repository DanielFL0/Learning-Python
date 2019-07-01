#8-3 T-Shirt; Write a fucntion called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
#The function should print a sentence summarizing the size of the shirt and the message printed o it.
#Call the function once using positional arguments to make a shirt. 
#Call the function a second time using keyword arguments.

def make_shirt(size, message):
    """Display the size and message printed on the T-Shirt"""
    print("The T-Shirt size is: " + size + "\nThe message is: " + message)

#Using positional arguments
make_shirt('large', 'I love Python!')

#Using keyword arguments
make_shirt(size='large', message='I love Python!')
