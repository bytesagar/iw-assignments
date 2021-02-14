def largest_of_all(items):
    max_ = items[0]
    for i in items:
        max_ = i if i > max_ else max_
    return max_
print(largest_of_all([1,2,3,4,5]))