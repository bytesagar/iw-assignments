def remove_dup(items):
    item = items[0]

    for i in items:
        if item == i:
            items.remove(item)
        else:
            return items
print(remove_dup([1,2,3,4,5,1,2]))