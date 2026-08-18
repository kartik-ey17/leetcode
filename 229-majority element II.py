def majority(nums):
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n , 0)
    return [k for k,v in count.items() if v> len(nums)/3 ]
print(majority([1,2,1,2,1,1,2]))