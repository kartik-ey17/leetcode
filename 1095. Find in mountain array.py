def findInMountainArray(target,mountainArr):
    n = mountainArr.length()
    l = 0
    r = n-1
    while l < r:
        mid = (l+r)//2
        if mountainArr.get(mid) > mountainArr.get(mid+1):
            r = mid
        else:
            l = mid + 1
    peak = l

    l = 0
    r = peak
    while l <= r:
        mid = (l+r)//2
        if target == mountainArr.get(mid):
            return mid
        elif mountainArr.get(mid) > target:
            r = mid - 1
        else:
            l = mid + 1

    l = peak+1
    r = n-1
    while l <= r:
        mid = (l+r)//2
        if target == mountainArr.get(mid):
            return mid
        elif mountainArr.get(mid) > target:
            l = mid + 1
        else:
            r = mid - 1
    return -1