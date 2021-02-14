from typing import List
def multiplier(items: List):
    res = 1
    for i in items:
        res = res * i
    return res
print(multiplier([1,2,3]))