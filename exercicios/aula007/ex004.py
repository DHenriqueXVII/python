n = int(input('Informe um número: '))

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

def raizQ(n):
    return n ** (1 / 2)

print(f'O dobro de {n} é {dobro(n)}, o triplo é {triplo(n)} e a raiz quadrada é {raizQ(n):.2f}')