def minEatingSpeed(piles,h):
    def can_eat(k):
        hours = 0

        for pile in piles:
            hours += (pile + k - 1) // k
        return hours <= h
    l = 1
    r = max(piles)
    while l < r:
        mid = (l+r) // 2
        if can_eat(mid):
            r = mid
        else:
            l = mid + 1
    return l
print(minEatingSpeed([30,11,23,4,20] , 5))