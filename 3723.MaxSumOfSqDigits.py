class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        res = []
        for _ in range(num):
            digit = min(9,sum)
            res.append(str(digit))
            sum -= digit
        return "".join(res) if sum == 0 else ""