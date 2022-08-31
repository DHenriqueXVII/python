salario = float(input('Informe o salário: '))

if salario > 1250:
    aumento = salario + salario * 10/100

    print(f'O salário teve um aumento de 10% e agora vale {aumento}')
else:
    aumento = salario + salario * 15/100

    print(f'O salário teve um aumento de 15% e agora vale {aumento}')