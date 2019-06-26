#5-1 Conditional tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test.
#Look closely at your results, and make sure you understand why each line evaluates to True or False.
#Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

name = 'daniel'
print("Is name == 'daniel'? I predict True.")
print(name == 'daniel')

print("Is name == 'danny'? I predict False.")
print(name == 'danny')

value1 = 6
value2 = 10
print("Is value1 == 6? I predict True")
print(value1 == 6)

print("Is value2 == 6? I predict False")
print(value2 == 6)

total = 6 + 10
print("Is total == 16? I predict True.")
print(total == 16)

print("Is total == 20? I predict False.")
print(total == 20)

print("Is value1 >= 3 and value2 >= 3? I predict True")
print(value1 >= 3 and value2 >= 3)

print("Is value1 <= 3 and value2 <= 3? I predict False")
print(value1 <= 3 and value2 <= 3)

print("Is value1 >= 3 or value2 <= 3? I predict True")
print(value1 >= 3 or value2 <= 3)

print("Is value1 <= 5 or value2 <= 3? I predict False")
print(value1 <= 5 or value2 <= 3)
