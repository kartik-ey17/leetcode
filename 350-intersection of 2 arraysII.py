def intersection(nums1,nums2):
    count = {}
    for n in nums1:
        count[n] = 1 + count.get(n, 0)
    r = []
    for n in nums2:
        if count.get(n, 0) > 0:
            r.append(n)
            count[n] -= 1
    return r


print(intersection([1,2,2,1],[2]))