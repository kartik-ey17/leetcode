def numSubarrayProductLessThanK(nums , k):
    if k <= 1:
        return 0
    l = 0
    p = 1
    res = 0

    for r in range(len(nums)):
        p *= nums[r]
        while p >= k:
            p //= nums[l]
            l += 1
        res += r - l + 1
    return res
print(numSubarrayProductLessThanK([1,2,3] , 0))