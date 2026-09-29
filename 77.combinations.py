def combine(n,k):
    res = []
    def backtrack(remain , comb , next):
        if remain == 0:
            res.append(comb.copy())
            return
        else:
            for i in range(next,n+1):
                comb.append(i)
                backtrack(remain-1 , comb , i+1)
                comb.pop()
    backtrack(k,[],1)
    return res
print(combine(4,2))