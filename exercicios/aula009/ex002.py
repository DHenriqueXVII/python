nome = str(input('Informe seu nome: ')).strip()
totLetras = ''.join(nome.split())
totLetras = len(totLetras)

print(f'Seu nome em letras maiúsculas: {nome.upper()}')
print(f'Seu nome em letras minúsculas: {nome.lower()}')
print(f'Seu nome tem {totLetras} letras')

totLetras = nome.split()
totLetras = len(totLetras[0])

print(f'Seu primeiro nome tem {totLetras} letras')
