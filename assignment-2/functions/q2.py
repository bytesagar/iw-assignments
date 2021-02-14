from typing import List
def add_items(items: List):
    sum = 0
    for i in items:
        sum += i
    return sum
print(add_items([1,3,4,4]))