n1 = float(input('Informe o primeiro número: \33[1;32m'))
n2 = float(input('\33[mInforme o segundo número: \33[1;32m'))

if n1 > n2:
    print('\n\33[mO primeiro número é maior!')
elif n1 == n2:
    print('\n\33[mOs números são iguais!')
else:
    print('\n\33[mO segundo número é maior!')