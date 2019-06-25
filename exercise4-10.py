#4-10 Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#Print the message, The first three items in the list are:. Then use a slice to print the first three items from that program's list.
#Print the message, Three items from the middle of the list are:. Use a slice top print three items from the middle of the list.
#Print the messages, The last three items in the list are:. Use a slice to print the last three items in the list.

#Using exercise 4-9
cubes_list = [value**3 for value in range(1, 11)]
print(cubes_list)

#We can also just omit the first index instead of using 0, by doing this the output will be exactly the same.
print("The first three items in the list are: " + str(cubes_list[0:3]))

print("Three items from the middle of the list are; " + str(cubes_list[2:5]))

print("The last three items in the list are: " + str(cubes_list[-3:]))
