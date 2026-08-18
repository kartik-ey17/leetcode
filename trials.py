s = 'leetcode'
count = {}
for i in s:
    count[i] = 1+ count.get(i, 0)
    print(count)
for k,v in count.items():
    if v == 1:
        print(k)
        break