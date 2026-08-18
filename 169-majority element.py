def majority(nums):
    countN = {}
    for n in nums:
        countN[n] = 1 + countN.get(n , 0)
    return sorted(countN, key= lambda n: (-countN[n] , n))[0]
print(majority([2,1,1,1,1,2,2]))