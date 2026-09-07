"""
[1,2],[-2,-1],[-1,2],[0,2] #arrays
find the number of 4-number combinations whose sum is 0
1. (0,0,0,1){indices} -> 1+(-2)+(-1)+2 = 0
2. (1,1,0,0){indices} -> 2+(-1)+(-1)+0 = 0
no other 4 number combination from the given arrays equate to 0 
=> output is 2
"""
from collections import defaultdict
def four_sum(nums1,nums2,nums3,nums4):
    h_map = defaultdict(int)
    four_sum = 0
    for n1 in nums1:
        for n2 in nums2:
            h_map[n1 + n2] += 1

    for n3 in nums3:
        for n4 in nums4:
            four_sums += h_map[-(n3+n4)]
    return four_sum