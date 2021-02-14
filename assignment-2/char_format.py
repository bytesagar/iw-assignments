def str_format(str):
    if len(str) < 2:
        return ""
    else:
        return str[0:2] + str[-2:]
print(str_format("Python"))

