#3-10 Every function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you'd like. Write a program that creates a list containing these items and then uses each function introduced in this chapter t least once.

programming_languages = ['Python', 'Java', 'C++', 'C#', 'C']

#Lets start by using the index in our list
print("My 2 favorite programming languages are: " + programming_languages[0] + " and " + programming_languages[2])

#In the next line, i'm going to edit Java for Ruby
programming_languages[1] = 'Ruby'
print(programming_languages)

#Next I will add 3 programming languages using insert() and append()
programming_languages.insert(2, 'Java')
print(programming_languages)
programming_languages.insert(3, 'JavaScript')
print(programming_languages)
programming_languages.append('Lua')
print(programming_languages)

#Next I will remove 3 programming languages using pop(), remove(), and del
programming_languages.pop()
print(programming_languages)
programming_languages.remove('JavaScript')
print(programming_languages)
del programming_languages[1]
print(programming_languages)

#Next I will sort my list with the methods sorted(), sort() and reverse()
print(sorted(programming_languages))
print(sorted(programming_languages, reverse=True))
programming_languages.sort()
print(programming_languages)
programming_languages.sort(reverse=True)
print(programming_languages)
programming_languages.reverse()
print(programming_languages)

#Next I will find the length of my list
print(len(programming_languages))
