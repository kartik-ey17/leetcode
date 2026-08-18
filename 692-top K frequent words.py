def topk(words , k):
    countW = {}
    for w in words:
        countW[w] = 1 + countW.get(w , 0)
    return sorted(countW , key=lambda w:(-countW[w] , w))[:k]
print(topk(['a','b','a','b'] , 2))