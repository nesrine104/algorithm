n = int(input())
for i in range (1, n+1):
    res = i*i*(i*i-1) - 8 - 24 - 16*(i-4) - 16 - 24*(i-4) - 8*(i-4)**2 
    print(res//2)