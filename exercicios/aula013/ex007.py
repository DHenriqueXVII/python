primeiroTermo = int(input('Informe o primeiro termo da progressão aritmética: \33[1;32m'))
razao = int(input('\33[mInforme a razão da progressão aritmética: \33[1;32m'))

pa = primeiroTermo

print('\n\33[mPrimeiros 10 termos da progressão aritmética:\n')

for contador in range(1, 11):
    print(pa, end=" -> ")

    pa += razao

print('ACABOU!')