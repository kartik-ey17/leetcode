"""
[1,2],[-2,-1],[-1,2],[0,2] #arrays
find the number of 4-number combinations whose sum is 0
1. (0,0,0,1){indices} -> 1+(-2)+(-1)+2 = 0
2. (1,1,0,0){indices} -> 2+(-1)+(-1)+0 = 0
no other 4 number combination from the given arrays equate to 0 
=> output is 2
"""
def foursum(nums1,nums2,nums3,nums4):
    sol = 0
    for i in nums1:
        for j in nums2:
            for k in nums3:
                for l in nums4:
                    if i+j+k+l == 0:
                        sol += 1
    return sol

print(foursum([1,2] , [-2,-1] , [-1,2] , [0,2]))