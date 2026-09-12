def maximumScore(nums,k):
    l = k
    r = k
    min_val = nums[k]
    max_scr = min_val
    while l > 0 or r < len(nums) - 1:
        if l == 0 or (r<len(nums)-1 and nums[r+1] > nums[l-1]):
            r += 1
        else:
            l -= 1
        min_val = min(min_val, nums[l] , nums[r])
        max_scr = max(max_scr , min_val*(r-l+1))
    return max_scr

print(maximumScore([5,5,4,5,4,1,1,1] , 0))