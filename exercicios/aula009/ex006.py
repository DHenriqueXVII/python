frase = str(input('Digite alguma coisa: ')).replace(' ', '')

a = frase.lower().count('a')

b = frase.lower().find('a')

print(f'A letra "A" aparece {a} vezes')

print(f'A letra "A" aparece pela primeira vez na posição {b}')

i = 0

posicoes = []

while i < len(frase):
    if 'a' in frase[i]:
        posicoes.append(i)
    i += 1

print(f'A letra "A" aparece pela última vez na posição {posicoes[-1]}')
