from collections import defaultdict
strs = ['cat' , 'bat' , 'tab' , 'tac' , 'mat']
res = defaultdict(list)
for s in strs:
    count = [0]* 26
    for c in s:
        count[ord(c) - ord('a')] += 1
        print(count)
    print(res)
    res[tuple(count)].append(s)
print(list(res.values()))