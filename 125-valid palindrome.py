s = 'A man, a plan, a canal: Panama'
result = ''
for ch in s:
    if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
        result += ch.lower()
rev = result[::-1]
print(result)
print(rev)

if result == rev :
    print("valid palindrome")
else:
    print("non")