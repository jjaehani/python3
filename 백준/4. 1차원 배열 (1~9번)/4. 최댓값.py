l = []
for i in range(9):
    n = int(input())
    l.append(n)

print(max(l))
print(l.index(max(l))+1)