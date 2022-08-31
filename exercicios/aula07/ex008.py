dinheiro = float(input('Valor em R$: '))

def conversao(dinheiro):
    return dinheiro / 3.27

print(f'Você pode comprar ${conversao(dinheiro):.2f}')