def maxProduct(nums):
    curr_max = nums[0]
    curr_min = nums[0]
    ans = nums[0]
    for i in range(1, len(nums)):
        x = nums[i]
        old_max = curr_max
        curr_max = max(x , x * curr_min , x * curr_max)
        curr_min = max(x , x*old_max , x*curr_min)
        ans = max(ans , curr_max)
    return ans
