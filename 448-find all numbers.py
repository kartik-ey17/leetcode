def disappeared(nums):
    s = set(nums)
    r =[]
    for i in range(1,len(nums)+1):
        if i not in s:
            r.append(i)
    return r

print(disappeared([4,3,2,7,8,2,3,1]))
