def insert_into_list(items,string):
    items = items.copy()
    for i in range(len(items)):
        items[i] = string + str(items[i])
    return items

