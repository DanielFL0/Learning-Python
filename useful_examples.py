#Looping through dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
print(favorite_languages.keys())
print(favorite_languages.items())

for name, language in favorite_languages.items():
    print("Name: " + name)
    print("Language: " + language)

for name in sorted(favorite_languages.keys()):
    print("Name: " + name)

for language in favorite_languages.values():
    print("Language: " + language)

#Using set (Set values must be unique)
for language in set(favorite_languages.values()):
    print("Language: " + language)
