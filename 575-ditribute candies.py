def alice(nums):
    l = len(nums)//2
    s = set()
    for c in nums:
        s.add(c)
        if len(s) == l:
            return l
    return len(s)

print(alice([1,1,2,3]))