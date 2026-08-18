def diff(s,t):
    count = {}
    for char in s:
        count[char] = 1+ count.get(char , 0)
    print(count)
    print(count[char])
    for char in t:
        if char not in count or count[char] == 0:
            return char
        print(count[char])
        count[char] -= 1

print(diff("abcd" , "abcde"))