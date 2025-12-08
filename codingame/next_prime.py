def is_prime(n):
    i = 2
    f = abs(n // 2)
    while i < f:
        if n % i == 0:
            return False
        i += 1
    return True

def next_prime(n):
    while not is_prime(n):
        n += 1
    return n

m = int(input())
for i in range(m):
    n = int(input())
    print(next_prime(n))