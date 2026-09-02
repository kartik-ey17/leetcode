def totalFruit(fruits):
    count = {}
    l = 0
    res = 0
    for r in range(len(fruits)):
        count[fruits[r]] = count.get(fruits[r] , 0) + 1

        while len(count) > 2:
            count[fruits[l]] -= 1
            if count[fruits[l]] == 0:
                del count[fruits[l]]
            l += 1
        res = max(res , r-l+1)
    return res
print(totalFruit([1,2,3,2,2]))