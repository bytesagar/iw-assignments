def insert_str_mid(braces: str,string: str):
    center_idx = int(len(braces) / 2)
    result = braces[:center_idx] + string + braces[center_idx:]

    return result
print(insert_str_mid('[[]]','sagar'))