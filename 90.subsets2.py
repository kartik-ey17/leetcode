def subsetsWithDup(nums):
    result = []
    path = []
    nums.sort()
    def backtrack(i):
        if i == len(nums):
            if path not in result:
                result.append(path.copy())
            return
        path.append(nums[i])
        backtrack(i+1)
        path.pop()
        backtrack(i+1)
    backtrack(0)
    return result

print(subsetsWithDup([4,4,4,1,4]))