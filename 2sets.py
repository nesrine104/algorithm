n = int(input())
a = set()
b = set()
m = n*(n+1)//2
if m % 2 == 0:
    print('YES')
    for i in range (n, 0, -1):
        if sum(a)>sum(b):
            b.add(i)
        else: a.add(i)
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)
else:
    print('NO')