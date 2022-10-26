from random import randint
from time import sleep

print(
"""Suas opções:
    
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura"""
)

opcoes = ['pedra', 'papel', 'tesoura']

escolhaUsuario = int(input('\nQual é a sua jogada ? \33[1;32m'))
escolhaMaquina = randint(0, 2)

sleep(0.5)

print('\n\33[m\33[1;33mJO')

sleep(0.5)

print('KEN')

sleep(0.5)

print('PO\33[m')

sleep(0.5)

print(f'\nComputador jogou \33[1;32m{opcoes[escolhaMaquina]}\33[m')
print(f'Jogador jogou \33[1;32m{opcoes[escolhaUsuario]}\33[m')

if escolhaUsuario == escolhaMaquina:
    print('\n\33[1;33mEMPATE!\33[m')
elif escolhaUsuario == 0 and escolhaMaquina == 2 or escolhaUsuario == 1 and escolhaMaquina == 0 or escolhaUsuario == 2 and escolhaMaquina == 1:
    print('\n\33[1;32mVITÓRIA DO JOGADOR!\33[m')
else:
    print('\n\33[1;31mVITÓRIA DO COMPUTADOR!\33[m')