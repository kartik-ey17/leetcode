def topk(nums,k):
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n , 0)
    return sorted(count , key= lambda n:(-count[n] , n))[:k]
print(topk([1,2,1,2,1,2,3,1,3,2] , 2))