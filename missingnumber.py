n = int(input())
a = map(int, input().split())
b = sum(a)
c = n*(n+1)//2
print(c-b)