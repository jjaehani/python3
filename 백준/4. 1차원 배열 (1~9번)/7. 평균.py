subject = int(input())
score = list(map(int, input().split()))
fake = ((sum(score)/subject) / max(score)) * 100
print(fake)
