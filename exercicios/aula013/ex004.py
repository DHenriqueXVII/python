quantidade_impares = 0
soma_impares = 0

for contador in range(1, 501):
    if contador % 3 == 0 and contador % 2 != 0:
        quantidade_impares += 1
        soma_impares += contador

print(f'A soma de todos os {quantidade_impares} valores solicitados é igual a {soma_impares}')