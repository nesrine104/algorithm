def gray_code(n):
    if n == 1:
        return ['0', '1']
    a = gray_code(n - 1)
    c1 = ['0' + code for code in a]
    c2 = ['1' + code for code in reversed(a)]
    return c1 + c2
    
n = int(input())
res = gray_code(n)
for i in res:
    print(i)