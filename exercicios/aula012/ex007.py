from datetime import date

data = date.today()
anoAtual = data.year

anoNascimento = int(input('Informe o ano de nascimento: \33[1;32m'))

idade = anoAtual - anoNascimento

if idade < 10:
    print(f'\n\33[mO atleta tem {idade} anos.')
    print(f'Classificação: MIRIM')
elif idade < 15:
    print(f'\n\33[mO atleta tem {idade} anos.')
    print(f'Classificação: INFANTIL')
elif idade < 20:
    print(f'\n\33[mO atleta tem {idade} anos.')
    print(f'Classificação: JUNIOR')
elif idade < 26:
    print(f'\n\33[mO atleta tem {idade} anos.')
    print(f'Classificação: SENIOR')
else:
    print(f'\n\33[mO atleta tem {idade} anos.')
    print(f'Classificação: MASTER')