intersec = lambda a1, a2: [x for x in a1 for y in a2 if x == y]

print(intersec([1,2],[2,3]))