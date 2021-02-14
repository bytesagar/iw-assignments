def remover(items,item):
    res = list(items)
    res.remove(item)
    return tuple(res)
print(remover((1,2,3,4),4))