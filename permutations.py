n = int(input())
if n == 1:
    print(n)
elif n < 4:
    print('NO SOLUTION')
else:
    for i in range (2, n+1, 2):
        print(i, end=' ')
    for i in range (1, n+1, 2):
        print(i, end=' ')