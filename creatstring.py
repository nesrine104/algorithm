import itertools
a = input().strip()
kq = set(itertools.permutations(a))
kq = sorted([''.join(p) for p in kq])
print(len(kq))
for i in kq:
    print(i)
