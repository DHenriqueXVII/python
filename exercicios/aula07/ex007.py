numero = int(input('Informe um número: '))

def tabuada(numero):
    indice = 1

    while indice <= 10:
        resultado = numero * indice
        print(f'{numero} x {indice} = {resultado}')
        indice += 1

tabuada(numero)