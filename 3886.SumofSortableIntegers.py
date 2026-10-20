class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        def check(k):
            prev = 0
            for i in range(0 , n , k):
                blk = nums[i:i + k]
                count = sum(blk[j] > blk[j+1] for j in range(k-1))
                if blk[-1] > blk[0]:
                    count += 1
                if count > 1 or prev > min(blk):
                    return False
                prev = max(blk)
            return True
        res = 0
        for k in range(1 , int(n**0.5) + 1):
            if n%k == 0:
                if check(k):
                    res += k
                other = n // k
                if other != k and check(other):
                    res += other
        return res