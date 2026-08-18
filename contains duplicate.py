def containsduplicate(nums) :
    hmap ={}
    for i,n in enumerate(nums):
        if n in hmap:
            return True
        hmap[n] = i
    return False

print(containsduplicate([1,2,3,4,5,6]))


"""

i      n
0      1
1      2
2      3
3      1

"""