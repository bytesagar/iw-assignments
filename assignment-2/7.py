def find_longest(words):
    lengths = map(len,words)
    return max(lengths)

print(find_longest(['hi','hello']))