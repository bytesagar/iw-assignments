from typing import List
def even_finder(list: List):
    even_list = []
    for i in list:
        if i % 2 == 0:
            
            even_list.append(i)
    return even_list
print(even_finder([1,2,3,4,5]))
