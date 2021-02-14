string = input("Enter a string: ")

f, *rem ,l = string

result = l + "".join(rem) + f

print(result)