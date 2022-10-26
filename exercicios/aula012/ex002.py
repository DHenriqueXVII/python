valor = float(input('Informe o valor da casa: R$ \33[1;32m'))
salario = float(input('\33[mInforme o seu salário: R$ \33[1;32m'))
anos = int(input('\33[mEm quantos anos deseja pagar ? \33[1;32m'))

print(f'\n\33[mPara pagar um empréstimo de R$ {valor:.2f} em {anos} anos a prestação será de R$ {(valor / (12 * anos)):.2f}')

if (valor / (12 * anos)) <= (salario * 30 / 100):
    print('\n\33[1;32mSeu empréstimo foi APROVADO!\33[m')
else:
    print('\n\33[1;31mSeu empréstimo foi NEGADO!\33[m')