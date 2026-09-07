def frequencySort(s):
    count = [0]*128
    for c in s:
        count[ord(c)] += 1
    chars = []
    for i in range(128):
        if count[i] > 0:
            chars.append((count[i] , chr(i)))
    chars.sort(reverse=True)

    res = ""

    for freq , char in chars:
        res += char*freq
    return res