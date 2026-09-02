def canJump(nums):
    farthest = 0
    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest,i+nums[i])
    return True
print(canJump([3,2,1,0,4]))