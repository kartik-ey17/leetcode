def maxDepthAfterSplit(seq):
    res = [0]*len(seq)
    depth = 0
    for i, ch in enumerate(seq):
        if ch == "(":
            depth += 1
            res[i] = depth %2
        else:
            res[i] = depth % 2
            depth -= 1
    return res
print(maxDepthAfterSplit("(()())"))