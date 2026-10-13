class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        s = sorted(x*x for x in nums)
        l = len(nums) //2
        return sum(s[l:]) - sum(s[:l])