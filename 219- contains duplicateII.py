def duplicate(nums, k):
    hmap = {}
    for i in range(len(nums)):
        if nums[i] in hmap and abs(i - hmap[nums[i]]) <= k:
            return True
        hmap[nums[i]] = i
    return False

print(duplicate([1,2,3,1,2,3] , 2))