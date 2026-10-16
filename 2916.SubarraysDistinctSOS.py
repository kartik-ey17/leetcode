class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        bit1 = [0] * (n+1)
        bit2 = [0] * (n+1)
        last = [-1] * 100001
        def prefix_sum(k):
            s1 = s2 = 0
            index = k
            while index > 0:
                s1 += bit1[index]
                s2 += bit2[index]
                index -= index & -index
            return k*s1-s2
        def add_boundary(index , delta):
            weighted = delta * (index - 1)
            while index <= n:
                bit1[index] += delta
                bit2[index] += weighted
                index += index & -index
        total_distinct = 0
        ending_sq = 0
        res = 0
        for i , value in enumerate(nums):
            l = last[value]
            affected_sum = total_distinct - prefix_sum(l+1)
            length = i - l
            ending_sq = (ending_sq + 2 * affected_sum + length) % mod
            res = (res+ending_sq) % mod
            add_boundary(l+2 , 1)
            add_boundary(i+2 , -1)
            total_distinct += length
            last[value] = i
        return res