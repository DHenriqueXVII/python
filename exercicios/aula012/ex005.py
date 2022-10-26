from datetime import date

dataAtual = date.today()

anoNascimento = int(input('Informe o ano em que você nasceu: \33[1;32m'))

if dataAtual.year - anoNascimento < 18:
    print(f'\n\33[mQuem nasceu em {anoNascimento} tem {dataAtual.year - anoNascimento} ano(s) em {dataAtual.year}.')
    print(f'Ainda falta(m) {18 - (dataAtual.year - anoNascimento)} ano(s) para o alistamento.')
    print(f'Seu alistamento será em {18 - (dataAtual.year - anoNascimento) + dataAtual.year}.')
elif dataAtual.year - anoNascimento == 18:
    print(f'\n\33[mQuem nasceu em {anoNascimento} tem {dataAtual.year - anoNascimento} ano(s) em {dataAtual.year}.')
    print('Você tem que se alistar IMEDIATAMENTE.')
else:
    print(f'\n\33[mQuem nasceu em {anoNascimento} tem {dataAtual.year - anoNascimento} ano(s) em {dataAtual.year}.')
    print(f'Você já deveria ter se alistado há {dataAtual.year - anoNascimento - 18} ano(s).')
    print(f'Seu alistamento foi em {dataAtual.year - (dataAtual.year - anoNascimento - 18)}.')
