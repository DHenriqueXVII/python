from random import shuffle

alunos = [
    input('Informe o nome do 1º aluno: '),
    input('Informe o nome do 2º aluno: '),
    input('Informe o nome do 3º aluno: '),
    input('Informe o nome do 4º aluno: ')
]

shuffle(alunos)

print(f'Ordem de apresentação \n1º {alunos[0]}\n2º {alunos[1]}\n3º {alunos[2]}\n4º {alunos[3]}')