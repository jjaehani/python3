n = []

for i in range(10):
    k = int(input())
    ans = k % 42
    n.append(ans)

final = set(n)
print(len(final))