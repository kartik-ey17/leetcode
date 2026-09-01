def findAnagrams(s,p):
    if len(s) < len(p):
        return 0
    count1 = [0] * 26
    count2 = [0] * 26

    for c in p :
        count1[ord(c) - ord('a')] += 1
    for i in range(len(p)):
        count2[ord(s[i]) - ord('a')] += 1
    res = []
    if count1 == count2:
        res.append(0)
    for r in range(len(p) , len(s)):
        count2[ord(s[r]) - ord('a')] += 1
        l = r - len(p)
        count2[ord(s[l]) - ord('a')] -= 1
        if count1 == count2:
            res.append(l+1)
    return res
print(findAnagrams('abab' , 'ab'))