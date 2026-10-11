class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in (range(n)):
            i += 1
            if n%i == 0:
                res += nums[i-1]*nums[i-1]
        
        return res