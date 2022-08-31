m = float(input('Informe um valor em metros: '))

def conversao(m):
    return [m * 100, m * 1000]

print(f'Valor convertido em centímetros: {conversao(m)[0]} \nValor convertido em milímetros: {conversao(m)[1]}')