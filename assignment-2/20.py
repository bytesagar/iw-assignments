def counter(items):
    count = 0
    for i in items:
        if len(i) >=2 and (i[0] == i[-1]):
            count += 1
    return count

print(counter(['abc','xyz','aba','1221']))