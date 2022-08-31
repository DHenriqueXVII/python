nome = str(input('Digite seu nome: ')).strip()

print('Olá, Diego, saudades de você!' if nome.lower() == 'diego' else f'Olá, {nome}, prazer em conhecê-lo!')