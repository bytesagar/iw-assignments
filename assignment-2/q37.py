def multiplier(items):
    res = 1
    for i in items.values():
        res *= i
    return res
print(multiplier({"a":2,"b":3,"c":4}))