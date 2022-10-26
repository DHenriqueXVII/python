numero = int(input('Informe um número inteiro: \33[1;32m'))

print(
"""
\33[mEscolha uma das bases para conversão:

[ 1 ] Converter para \33[1;33mBINÁRIO\33[m
[ 2 ] Converter para \33[1;33mOCTAL\33[m
[ 3 ] Converter para \33[1;33mHEXADECIMAL\33[m
"""
)

escolha = int(input('\nQual a sua opção ? \33[1;32m'))

if escolha == 1:
    print(f'\n\33[1;32m{numero}\33[m convertido para \33[1;33mBINÁRIO\33[m é igual a \33[1;32m{bin(numero)}\33[m')
elif escolha == 2:
    print(f'\n\33[1;32m{numero}\33[m convertido para \33[1;33mOCTAL\33[m é igual a \33[1;32m{oct(numero)}\33[m')
elif escolha == 3:
    print(f'\n\33[1;32m{numero}\33[m convertido para \33[1;33mHEXADECIMAL\33[m é igual a \33[1;32m{hex(numero)}\33[m')
else:
    print('\n\33[1;31mOpção inválida!\33[m')