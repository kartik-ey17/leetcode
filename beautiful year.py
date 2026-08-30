n=int(input())
n+=1
def check(n):
    a=str(n)
    s=set(a)
    if len(s)==len(a):
        return a
    else:
        return check(n+1)
print(check(n))