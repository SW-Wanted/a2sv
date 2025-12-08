# t = int(input())
# minimo = -(10**5)
# while t:
#     n = int(input())
#     minimo = min(abs(minimo), abs(n))
#     t -= 1
# print(abs(minimo))

t = int(input())
print(min(list(map(abs, map(int, input().split())))))