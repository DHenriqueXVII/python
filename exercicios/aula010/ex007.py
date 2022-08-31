from datetime import datetime


from datetime import date

ano = int(input('Informe o ano: '))

if ano == 0:
    ano = date.today().year

if (ano % 4 == 0 and not ano % 100 == 0) or (ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0):
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto!')