def pattern(nums):
    for i in range(len(nums)):
        if nums[i+1]>nums[i] and nums[i+1]>nums[i+2] and i+2 <= len(nums):
            return True
        else:
            return False
        
print(pattern([3,1,4,2]))