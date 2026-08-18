def duplicates(nums):
    l = []
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n , 0)
    for k,v in count.items():
        if v >= 2:
            l.append(k)
    return l
    
print(duplicates([4,3,2,7,8,2,3,1]))