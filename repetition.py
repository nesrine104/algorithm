a = input()
d = 1
m = 0
for i in range (1, len(a)):
    if a[i] == a[i-1]:
        d += 1 
    else:
        if d > m:
            m = d
        d=1
print(max(m, d))
    