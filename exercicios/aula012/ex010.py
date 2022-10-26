preco = float(input('Informe o preço da compra: R$ \33[1;32m'))

print(
"""
\33[mFORMAS DE PAGAMENTO

[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
"""
)

escolha = int(input('Qual a sua opção ? \33[1;32m'))

if escolha == 1:
    print(f'\n\33[mSua compra de R$ \33[1;32m{preco:.2f}\33[m vai custar R$ \33[1;32m{(preco - preco * 10 / 100):.2f}\33[m')
elif escolha == 2:
    print(f'\n\33[mSua compra de R$ \33[1;32m{preco:.2f}\33[m vai custar R$ \33[1;32m{(preco - preco * 5 / 100):.2f}\33[m')
elif escolha == 3:
    print(f'\33[mSua compra será parcelada em \33[1;32m2x\33[m de R$ \33[1;32m{(preco / 2):.2f}\33[m')
    print(f'Sua compra de R$ \33[1;32m{preco:.2f}\33[m vai custar R$ \33[1;32m{(preco):.2f}\33[m')
elif escolha == 4:
    parcelas = int(input('\n\33[mQuantas parcelas ? \33[1;32m'))

    print(f'\n\33[mSua compra será parcelada em \33[1;32m{parcelas}x\33[m de R$ \33[1;32m{(preco * 20 / 100 / parcelas + preco / parcelas):.2f}\33[m')
    print(f'\33[mSua compra de R$ \33[1;32m{preco:.2f}\33[m vai custar R$ \33[1;32m{(preco * 20 / 100 + preco):.2f}\33[m')
else:
    print(f'\n\33[mReinicie o programa e informe uma opção válida.')