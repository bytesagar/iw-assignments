from typing import List
def unique_creator(list: List):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(unique_creator([1,2,3,4,4,4,3,]))
    
