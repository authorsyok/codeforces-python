n, m = map(int, input().split())
a = list(map(int, input().split()))

count = 0

for _ in range(len(a)):
    if(a[_] > 0 and a[_] >= a[int(m) - 1]):
        count += 1

print(count)