def twosumtwo(nums,target):
    hmap = {}

    for i,n in enumerate(nums):
        diff = target -n
        if diff in hmap:
            return [hmap[diff] , i+1]
        hmap[n] = i+1

print(twosumtwo([-1,1] , 0))