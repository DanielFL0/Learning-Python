#6-3 Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let's call it a glossary.
#Think of five programming words you've learned about in the previous chapters. Use these words as the keys in your glossay, and store their meanings as values.
#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word meaning pair in your output.

programming_words = {
    'string': 'Sequence of characters.',
    'variable': 'Word that holds a value.',
    'list': 'A collection of any kind of data type.',
    'loop': 'Allows code to be executed repeatedly.',
    'slice': 'A portion of a list or tuple.'
    }
print("String: " + programming_words['string'] + "\n")
print("Variable: " + programming_words['variable'] + "\n")
print("List: " + programming_words['list'] + "\n")
print("Loop: " + programming_words['loop'] + "\n")
print("Slice: " + programming_words['slice'] + "\n")
