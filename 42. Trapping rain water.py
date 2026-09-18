"""
Approach -
    we bascially use 2 pointers ,
    l = 0 and r = len(array) - 1 ;
    and use a while loop till l < r 
    suppose array[l] is less than array[r] , then we do l += 1 , 
    and subtract the current l with the biggest l like ... 
    suppose an array [4,2,0,3,2,5] , l = 4 and r = 5 , 
    4 < 5 ; so we move l to 2 , 4> 2 : 4-2 = 2 ; 
    now l = 0 ; 4 > 0 : 4-0 = 4 ; 
    now l = 3 ; 4 > 3 : 4-3 = 1 ; 
    now l = 2 ; 4 > 2 : 4-2 = 2 ; 
    now l = 5 = r , so break , 
    now ,  2 + 4 + 1 + 2 = 9 which is the correct output for the test case
"""

def trap(height):
    l = 0
    r = len(height) - 1
    max_l = 0
    max_r = 0
    water = 0

    while l < r:
        if height[l] <= height[r]:
            if height[l] >= max_l:
                max_l = height[l]
            else:
                water += max_l - height[l]
            l += 1
        else :
            if height[r] >= max_r:
                max_r = height[r]
            else:
                water += max_r - height[r]
            r -= 1

    return water