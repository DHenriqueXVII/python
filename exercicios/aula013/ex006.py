soma = 0

for contador in range(1, 7):
    numero = int(input(f'\33[mInforme o {contador}º número: \33[1;32m'))

    if numero % 2 == 0:
        soma += numero

print(f'\n\33[mA soma entre os valores pares é igual a \33[1;32m{soma}\33[m')