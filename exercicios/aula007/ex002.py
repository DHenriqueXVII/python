n1 = int(input('Informe um número: '))
n2 = int(input('informe outro número: '))
e = n1 ** n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
a = n1 + n2
s = n1 = n2
print(f'Resultado da exponenciação: {e} \nResultado da multiplicação: {m} \nResultado da divisão: {d:.3f}', end=' ')
print(f'Resultado da divisão inteira: {di}')
print(f'Resultado da adição: {a}')
print(f'Resultado da subtração: {s}')