def item_replace(list1,list2):
    return [*list1[:-1], *list2]

print(item_replace([1,2,3],[4,5]))