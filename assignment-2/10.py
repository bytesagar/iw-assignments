string = input("Enter a string: ")
result = ""
for i,v in  enumerate(string):
    if i % 2 == 0:
        result += v
    
print(result)