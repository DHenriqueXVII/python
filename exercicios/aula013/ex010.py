from datetime import date

dataAtual = date.today()
anoAtual = dataAtual.year

menores = 0
maiores = 0

for contador in range(1, 8):
    anoDeNascimento = int(input(f'\33[mAno de nascimento da {contador}ª pessoa: \33[1;32m'))

    if anoAtual - anoDeNascimento < 21:
        menores += 1
    else:
        maiores += 1

print(f'\n\33[mMenores de idade: \33[1;32m{menores}\33[m')
print(f'Maiores de idade: \33[1;32m{maiores}\33[m')