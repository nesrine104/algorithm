import math
n = int(input())
count = 0
gt = math.factorial(n)
for i in range (1, n):
    if gt % 10 == 0:
        count += 1 
        gt = gt // 10
print(count)