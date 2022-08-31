distancia = float(input('Informe a distância da viagem: '))

if distancia > 200:
    valorPassagem = distancia * 0.45
else:
    valorPassagem = distancia * 0.50

print(f'O valor da sua passagem é {valorPassagem}')