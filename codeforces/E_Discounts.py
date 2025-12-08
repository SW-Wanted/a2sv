n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

t = sum(a)
a.sort(reverse=True)
for j in q:
    i = j - 1
    cost = a[i]
    minimo = t - cost
    print(minimo)