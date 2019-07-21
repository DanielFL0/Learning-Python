#9-13: OrderedDict Rewrite: Start with exercise6-4.py (page 108), where you
#used a standard dictionary to represent a glossary.
#Rewrite the program using the OrderedDict class and make sure the order of the
#output matches the order in which key-value pairs were added to the dictionary

from collections import OrderedDict

programming_words = OrderedDict()

programming_words['string'] = "Sequence of characters."
programming_words['variable'] = "Word that holds a value."
programming_words['list'] = "A collection of any kind of data type."
programming_words['tuple'] = "A fixed size collection of any kind of data "
programming_words['tuple'] += "type."
programming_words['if statements'] = "A condition which in case of being true"
programming_words['if statements'] += " executes a block of code."
programming_words['append()'] = "A method for adding elements to a list."
programming_words['del'] = "A method that deletes an item or the whole list."
programming_words['pop()'] = "A method that deletes the last item from a list."
programming_words['print()'] = "A method that prints text on a terminal."
programming_words['loop'] = "Allows code to be executed repeatedly."
programming_words['slice'] = "A portion of a list or tuple."

for word, meaning in programming_words.items():
    print("\n" + word.title() + ": " + meaning)
