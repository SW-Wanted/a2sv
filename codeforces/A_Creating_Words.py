n = int(input())
while n >= 1:
    a, b = (input().split())
    a, b = b[0] + a[1:], a[0] + b[1:]
    print(a, b)
    n -= 1