def help(nums,perk,k):
    count = 1
    s = 0
    for num in nums:
        if (s+num > perk):

            count += 1
            s = num
        else:
            s += num
    return count <= k

def splitArray(nums,k):
    high = sum(nums)
    low = max(nums)
    res = 0
    while low <= high:
        mid = low + (high-low)//2
        if help(nums,mid,k):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res
print(splitArray([1,2,3,4,5] , 2))