numero = int(input('Informe um número para saber se ele é primo: \33[1;32m'))

if numero < 2 or numero % 2 != 0:
    print(f'\33[mO número \33[1;32m{numero}\33[m não é primo!')
else:
    print(f'\33[mO número \33[1;32m{numero}\33[m é primo!')