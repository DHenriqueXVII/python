menor, maior = 0, 0

for contador in range(1, 6):
    peso = float(input(f'\33[mPeso da {contador}ª pessoa: \33[1;32m'))

    if contador == 1:
        menor = peso

    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'\n\33[mO menor peso foi: \33[1;32m{menor}\33[m')
print(f'O maior peso foi: \33[1;32m{maior}\33[m')