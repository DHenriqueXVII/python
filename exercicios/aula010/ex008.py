numeros = [
    float(input('Informe o primeiro número: ')),
    float(input('Informe o segundo número: ')),
    float(input('Informe o terceiro número: '))
]

print(f'\nO maior número é {sorted(numeros)[-1]}')
print(f'O menor número é {sorted(numeros)[0]}')