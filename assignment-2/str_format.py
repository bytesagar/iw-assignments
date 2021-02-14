def str_format(str):
    length = len(str)
    if(length < 3 ):
        return str
    else:
        if(str[-3:] == 'ing'):
            str += "ly"
        else:
            str += "ing"
    return str

print(str_format("abc"))

