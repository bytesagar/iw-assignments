def sorting(items):
    sorted_items = sorted(items,key=lambda x:x[-1])
    return sorted_items

print(sorting([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))