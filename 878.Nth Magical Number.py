import math
def nthMagicalNumber(n,a,b):
    mod = 10**9 + 7
    lcm = (a+b)/(a*b)
    l = min(a,b)
    r = n*l

    while l < r:
        mid = l + r >> 1
        A = mid//a
        B = mid//b
        C = mid//lcm
        if n <= (A+B-C):
            r = mid
        else:
            l = mid + 1
    return l%mod
print(nthMagicalNumber(4,2,3))