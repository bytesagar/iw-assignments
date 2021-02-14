string = input("Enter your string: ")
number = int(input("Enter your index: ")) # using array index.

result = string[0:number] + string[number+1:]

print(result)