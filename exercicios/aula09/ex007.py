nome = str(input('Informe seu nome: ')).strip()

print(f'Nome completo: {nome}')

print(f'Primeiro nome: {nome.split()[0]}')

print(f'Último nome: {nome.split()[-1]}')
