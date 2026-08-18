def unique(s):
    count = {}
    for n in s:
        count[n] = 1+ count.get(n, 0)
    for i,n in enumerate(s):
        if count[n] == 1:
            return i
    return -1

print(unique(''))