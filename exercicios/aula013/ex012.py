somaDasIdades = 0
maiorIdade = 0
homemMaisVelho = ''
mulheresMenoresDe20Anos = 0

for indice in range(1, 5):
    nome = str(input(f'\33[mNome da {indice}ª pessoa: \33[1;32m'))
    idade = int(input(f'\33[mIdade da {indice}ª pessoa: \33[1;32m'))
    sexo = str(input(f'\33[mSexo da {indice}ª pessoa \33[1;34mM\33[m / \33[1;31mF\33[m: \33[1;32m'))

    print()

    if sexo.lower() == 'm' or sexo.lower() == 'f':
        somaDasIdades += idade

        if idade > maiorIdade and sexo.lower() == 'm':
            maiorIdade = idade
            homemMaisVelho = nome

        if idade < 20 and sexo.lower() == 'f':
            mulheresMenoresDe20Anos += 1
    else:
        exit('\33[1;31mOpção inválida!\33[m')

media = somaDasIdades / 4

print(f'\n\33[mA média de idade é \33[1;32m{media}\33[m')
print(f'O homem mais velho é o \33[1;32m{homemMaisVelho}\33[m')
print(f'O número de mulheres com menos de 20 anos é \33[1;32m{mulheresMenoresDe20Anos}\33[m')