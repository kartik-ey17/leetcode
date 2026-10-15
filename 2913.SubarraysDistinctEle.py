class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = []
        for i in range(len(nums)):
            for j in range(i , len(nums) + 1):
                res.append(len(set(nums[i:j]))*len(set(nums[i:j])))
        return sum(res)