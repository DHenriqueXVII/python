numero = int(input('Informe um número para saber a sua tabuada: \33[1;32m'))

print(f'\n\33[mTabuada do número \33[1;32m{numero}\33[m\n')

for contador in range(1, 11):
    print(f'{numero} x {contador} = {numero * contador}')