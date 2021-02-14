str = input("Enter your string: ")

not_index = str.find("not")
poor_index = str.find("poor")
result = str
if not_index < poor_index and not_index != -1:
    first = str[:not_index]
    middle = "good"
    last = str[poor_index+4:]
    result = first + middle + last
print(result)