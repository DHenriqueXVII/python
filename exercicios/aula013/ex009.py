import unicodedata

frase = unicodedata.normalize('NFD', str(input('Informe a frase: ')).replace(' ', '').lower())
frase = frase.encode('ascii', 'ignore')
frase = frase.decode('utf-8')
palindromo = []

for contador in range(int(len(frase)), 0, -1):
    palindromo.append(frase[contador -1])

palindromo = ''.join(palindromo)

if frase == palindromo:
    print('A frase informada é um palindromo!')
else:
    print('A frase informada não é um palindromo!')