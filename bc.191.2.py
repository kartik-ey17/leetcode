def specialNumbers(nums):
    hmap = {}
    for i,n in enumerate(nums):
        if n not in hmap:
            hmap[n] = []
        hmap[n].append(i)
    res = 0
    for h in hmap.values():
        if len(h) > 3 :
            continue
        space = h[1] - h[0]
        s = True
        for i in range(2,len(h)):
            if h[i] - h[i-1] != space:
                s = False
                break
        if s:
            res += 1
    return res
print(specialNumbers([1,8,1,5,1,5,8,5]))