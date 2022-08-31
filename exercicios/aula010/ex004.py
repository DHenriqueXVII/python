velocidade = int(input('Qual a velocidade atual do carro ? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7

    print(f'\nVocê foi multado em R$ {multa} por excesso de velocidade.\n')

print('Tenha um bom dia! Dirija com segurança!')