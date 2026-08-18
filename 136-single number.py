def singleno(nums):
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n , 0)
        print(count)
    for k,v in count.items():
        print(k,v)
        if v == 1:
            return k
        
print(singleno([4,1,2,1,2]))