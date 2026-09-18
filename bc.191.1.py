def specialNumbers(nums):
    hmap = {}
    for i,n in enumerate(nums):
        if n not in hmap:
            hmap[n] = []
        hmap[n].append(i)
    res = 0
    for h in hmap.values():
        if len(h) == 3 and h[1] - h[0] == h[2] - h[1]:
            res += 1
    return res