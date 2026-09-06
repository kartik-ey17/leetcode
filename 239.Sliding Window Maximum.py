"""nums = [1,3,-1,-3,5,3,6,7]
k = 3
res = []
window = [0]*k
l = 0
r = k-1
n = l
while r < len(nums):
    for i in range(k+1):
        if n <= r:
            window[i] = nums[n]
            n += 1
    res.append(max(window))
    l += 1
    r += 1
    n = l
print(res) --- TLE"""
from collections import deque
def maxSlidingWindow(nums,k):
    res = []
    window = deque()
    l = 0
    r = 0
    while r < len(nums):
        while window and nums[window[-1]] < nums[r]:
            window.pop()
        window.append(r)
        if window[0] < 1:
            window.popleft()
        if r - l + 1 == k:
            res.append(nums[window[0]])
            l += 1
        r += 1
    return res