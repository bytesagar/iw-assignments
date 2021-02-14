def char_swap(str1,str2):
    char_1 = str1[-1]
    char_2 = str2[-1]
    res1 = str2[:-1] + char_1
    str2 = str1[:-1] + char_2
    return (res1 + " " + str2)
print(char_swap('abc','xyz'))