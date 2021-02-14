def max_of_three(a: int,b: int,c: int):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c
