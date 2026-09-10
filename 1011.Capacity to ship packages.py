
def shipWithinDays(weights,days):
    def feasible(cap):
        d = 1
        total = 0
        for weight in weights:
            total += weight
            if total > cap:
                total = weight
                d += 1
                if d > days:
                    return False
        return True
    l = max(weights)
    r = sum(weights)
    while l < r:
        mid = l + (r-l)//2
        if feasible(mid):
            r = mid
        else:
            l = mid + 1
    return l
print(shipWithinDays([1,2,3,4,5,6,7,8,9,10] , 5))
