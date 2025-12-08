n = int(input())
cubes = list(map(int, input().split()))
cubes.sort()
j = 0
while j < len(cubes) - 1:
    print(cubes[j], end=' ')
    j += 1
print(cubes[j])