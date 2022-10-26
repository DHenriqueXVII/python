from random import choice

alunos = [
    input('Informe o nome do 1º aluno: '),
    input('Informe o nome do 2º aluno: '),
    input('Informe o nome do 3º aluno: ' ),
    input('Informe o nome do 1º aluno: ' )
]

print(f'O aluno escolhido foi {choice(alunos)}')