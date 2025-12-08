# Primeiro os Pares : (0, n1), (0, n2), (0, n3)
# Depois os Ímpares : (1, n6), (1, n5), (1, n4)

def ordenar(numero):
    if numero % 2 == 0:
        return (0, numero)
    return (1, -numero)

n = int(input())
numeros = list()
while n > 0:
    v = int(input())
    numeros.append(v)
    n -= 1
numeros.sort(key=ordenar)
for i in numeros:
    print(i)