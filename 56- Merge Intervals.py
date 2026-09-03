def merge(intervals):
    intervals.sort()
    res = []
    for i in intervals:
        if not res or i[0] > res[-1][1]:
            res.append(i)
        else:
            res[-1][1] = max(res[-1][1] , i[1])
    return res
print(merge([[1,3],[2,6],[8,10],[15,18]]))