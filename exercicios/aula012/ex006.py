n1 = float(input('Informe a primeira nota: \33[1;32m'))
n2 = float(input('\33[mInforme a segunda nota: \33[1;32m'))

if n1 <= 10 and n2 <= 10:
    media = (n1 + n2) / 2

    if media < 5:
        print(f'\n\33[mTirando \33[1;31m{n1:.1f}\33[m e \33[1;31m{n2:.1f}\33[m a média é \33[1;31m{media:.1f}\33[m.')
        print('O aluno está \33[1;31mREPROVADO!\33[m')
    elif media < 7:
        print(f'\n\33[mTirando \33[1;33m{n1:.1f}\33[m e \33[1;33m{n2:.1f}\33[m a média é \33[1;33m{media:.1f}\33[m.')
        print('O aluno está na \33[1;33mRECUPERAÇÃO!\33[m')
    else:
        print(f'\n\33[mTirando \33[1;32m{n1:.1f}\33[m e \33[1;32m{n2:.1f}\33[m a média é \33[1;32m{media:.1f}\33[m.')
        print('O aluno está \33[1;32mAPROVADO!\33[m')
else:
    print('\n\33[mReinicie o programa e informe duas notas de 0 a 10.')