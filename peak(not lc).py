listt = [1,3,5,8,4,2,0]
peak = 1
l , r = 0 , 1
while r < len(listt) :
    if listt[l] > listt[r]:
        peak = listt[l]
        break
    elif r == len(listt) -1:
        peak = listt[r]
        break
    else:
        l += 1
        r += 1
print(peak)