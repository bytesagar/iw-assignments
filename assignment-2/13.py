string = input("Enter a string: ")

str_list = string.split(", ")
str_list.sort()

print(*str_list, sep=", ")