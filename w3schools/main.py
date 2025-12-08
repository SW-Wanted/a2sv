def pascal():
    n = 5
    for i in range(n):
        c = 1
        for j in range(n, i, -1):
            print(' ', end='')
        for j in range(i + 1):
            print(c, end=' ')
            c = c * ( (i + 1) - (j + 1) ) // (j + 1)
        print()

def identity():
    x = [1, 2, 3]
    y = [1, 2, 3]
    z = x
    print('x is y -> ', end='')
    print(x is y)
    print(f'x == y -> {x == y}')
    print('x is z -> ', end='')
    print(x is z)
    print(f'x == z -> {x == z}')
    print([1, 2] is [1, 2])

identity()