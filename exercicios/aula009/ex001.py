frase = 'Curso em Video Python'

print(frase[3:13:2])

print("""O Esporte Clube Vitória é um clube multiesportivo brasileiro, sediado na cidade de Salvador, no estado da Bahia.
Foi fundado em 13 de maio de 1899 com o nome de Club de Cricket Victoria, mudado para Sport Club Victoria, em 1902, e, finalmente, para o atual nome em 1946.""")

print(frase.count('o'))

print(frase.upper().count('O'))

print(len(frase.strip()))

print(frase.replace('Python', 'Android'))

print('Curso' in frase)

print(frase.find('Curso'))

print(frase.split())

print(frase.split()[2][3])

frase1 = frase.split()

print('_'.join(frase1))
