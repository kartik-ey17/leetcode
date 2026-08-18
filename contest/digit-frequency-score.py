def digitfreq(n):
    ans = 0
    while n :
        ans += n%10
        n //=10
    return ans

print(digitfreq(122))