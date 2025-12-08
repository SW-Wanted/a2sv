import math

# print(100 % 3)         1
# print(100 % -3)       -2
# print(-100 % 3)        2
# print(-100 % -3)      -1

mod = lambda n, m : int(math.fmod(n, m))

# N = 9, M = 3
# 1 % 3 = 1
# 2 % 3 = 2
# 3 % 3 = 0
# 4 % 3 = 1
# 5 % 3 = 2
# 6 % 3 = 0
# 7 % 3 = 1
# 8 % 3 = 2
# 9 % 3 = 0


# 3 % 3 = 0 # PAR
# 6 % 3 = 0 # PAR
# 9 % 3 = 0 # IMPAR
# 1 % 3 = 1 # IMPAR
# 4 % 3 = 1 # PAR
# 7 % 3 = 1 # IMPAR
# 2 % 3 = 2 # PAR
# 5 % 3 = 2 # IMPAR
# 8 % 3 = 2 # PAR

# -- EMPATE --
# IMPAR < PAR
# IMPAR < impar
# par < PAR

# 9 % 3 = 0 # IMPAR
# 3 % 3 = 0 # PAR
# 6 % 3 = 0 # PAR
# 7 % 3 = 1 # IMPAR
# 1 % 3 = 1 # IMPAR
# 4 % 3 = 1 # PAR
# 5 % 3 = 2 # IMPAR
# 2 % 3 = 2 # PAR
# 8 % 3 = 2 # PAR

def criterio_ordenacao(m):

    def ordem(n):
        is_impar = (n % 2 != 0)
        return (mod(n, m), -is_impar, n if not is_impar else -n)
    return ordem

def imprimir(lista):
    for i in lista:
        print(i)

while True:
    n, m = map(int, input().split())
    print(n, m)
    if n == m == 0:
        break;
    numeros = list()
    for _ in range(n):
        v = int(input())
        numeros.append(v)
    ordenar = criterio_ordenacao(m)
    numeros.sort(key=ordenar)
    imprimir(numeros)