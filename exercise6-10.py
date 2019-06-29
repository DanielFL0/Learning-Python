#6-10 Favorite numbers: Modify your program from exercise6-2 (page 102) so each person can have more than one favorite number. Then print each person's name along with their favorite numbers.

#Using exercise6-2
favorite_numbers = {
    'daniel': [1337, 123, 12],
    'samuel': [7, 4],
    'jose': [637, 15]
    }
for person, numbers in favorite_numbers.items():
    print(person.title() + "'s favorite numbers are: ")
    for number in numbers:
        print("\t" + str(number))
