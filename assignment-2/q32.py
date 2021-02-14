def dic_generator(n):
    result = dict()

    for i in range(1, n+1):
        result[i] = i * i
    return result
print(dic_generator(5))