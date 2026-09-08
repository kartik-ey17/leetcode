def numsSquares(n):
    memo = {0: 0}
    def solve(n):
        if n in memo:
            return memo[n]
        ans = float("inf")
        i = 1
        while i*i <=n:
            ans = min(ans,solve(n - i*i)+1)
            i += 1
        memo[n] = ans
        return ans
    return solve(n)