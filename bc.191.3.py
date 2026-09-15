def minDays(n):
    ans = float("inf")
    def solve(score,days):
        nonlocal ans
        if score == n:
            ans = min(ans,days)
            return
        if score > n or days >= ans:
            return
        k = 1
        while True:
            p = k*(k+1)//2
            if score + p > n:
                break
            solve(score + p, days +k + (1 if score > 0 else 0))
            k += 1
    solve(0,0)
    return ans
print(minDays(2))