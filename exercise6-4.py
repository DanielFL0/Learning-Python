#6-4 Glossary 2: Now that you know how to loop through a dictionary, clean up the code from exercise6-3 (page 102) by replacing your series of print statements with a loop that runs through the dictionary's keys and values.
#When you're sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

programming_words = {
    'string': 'Sequence of characters.',
    'variable': 'Word that hols a value.',
    'list': 'A collection of any kind of data type.',
    'tuple': 'A fixed size collection of any kind of data type.',
    'if statements': 'A condition which in case of being true executes a block of code.',
    'append()': 'A method for adding elements to a list.',
    'del': 'A method that deletes an item or the whole list.',
    'pop()': 'A method that deletes the last item from a list.',
    'print()': 'A method that prints text on a terminal.',
    'loop': 'Allows code to be executed repeatedly.',
    'slice': 'A portion of a list or tuple.'
    }
for word, meaning in programming_words.items():
    print("\n" + word.title() +": " + meaning)
