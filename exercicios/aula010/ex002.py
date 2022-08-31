n1 = float(input('informe a nota da 1ª unidade: '))
n2 = float(input('informe a nota da 2ª unidade: '))
m = (n1 + n2) / 2

if m < 5:
    print(f'Você foi reprovado com a média {m}')
else:
    print(f'Você foi aprovado com a média {m}')