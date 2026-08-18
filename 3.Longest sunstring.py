def longest(s):
    seen = set()
    left = 0
    r = 0
    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[i])
        r= max(r, i-left+1)
    return r
print(longest("abcabcbb"))