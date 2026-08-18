def twice(s):
    count = {}
    for n in s:
        count[n] = 1 + count.get(n, 0)
        if count[n] > 1:
            return n
    return None
print(twice('abcdd'))