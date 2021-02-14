def key_remover(item,key):
    item = item.copy()
    if  key in item:
        del item[key]
    return item