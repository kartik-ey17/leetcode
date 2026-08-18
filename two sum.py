def twosum(nums, target):
    hmap = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in hmap:
            return[hmap[diff] , i]
        hmap[n] = i
    return None

print(twosum([2,3,5,7] , 9))
