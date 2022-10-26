numero = input('Informe um número entre 0 e 9999: ')

print(f'Unidade: {numero[-1]}')
print(f'Dezena: {numero[-2:-1]}')
print(f'Centena: {numero[-3:-2]}')
print(f'Milhar: {numero[-4:-3]}')