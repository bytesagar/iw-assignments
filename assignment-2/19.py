def smallest_of_all(items):
    min_ = items[0]
    for i in items:
        min_  = i if i < min_ else min_
    return min_
print(smallest_of_all([1,2,3,4]))