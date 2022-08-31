dias = int(input('Quantos dias alugados ? '))
quilometragem = float(input('Quantos quilômetros rodados ? '))

print(f'O total a pagar é de R$ {dias * 60 + quilometragem * 0.15:.2f}')