def FindTargetSumWays(nums , target):
    s = sum(nums)
    res = s + target 
    if target > s or target < -s or res %2 == 1:
        return 0
    res //= 2
    dp = [0]* (res+1)
    dp[0] = 1
    for i in nums:
        for j in range(res , i-1 , -1):
            dp[j] += dp[j-i]
    return dp[-1]
print(FindTargetSumWays([1] , 1))