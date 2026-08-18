def colors(nums):
    count = [0,0,0]
    for n in nums:
        count[n] += 1
        print(count)
    index = 0

    for color in range(3):
        for _ in range(count[color]):
            nums[index] = color
            index += 1
    return nums
print(colors([0,1,2,0,2,1]))