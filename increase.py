n = int(input())
a = [int(i) for i in input().split()]
count = 0
for i in range (1, n):
    if a[i] < a[i-1]:
        count = count + a[i-1] -a[i]
        a[i] = a[i-1]
print(count)