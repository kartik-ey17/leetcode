nums = [-2,0,-1]
l = 0
p = []
for r in range(1,len(nums) ):
    p.append(nums[l]*nums[r])
    l += 1
product = max(p)
print(max(p))