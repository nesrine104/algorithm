a = input()
m = sorted(list(set(a)))
n = ''
half = ''
x = 0
for i in m:
    c = a.count(i)
    if c % 2 == 0:
        half += i * (c//2)
    elif x == 1:
        half = 0
        print('NO SOLUTION')
        break
    else:
        x = 1
        n = i 
        half += i * ((c-1)//2)
if half != 0: print(half + n + half[::-1])
