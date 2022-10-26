peso = float(input('Informe o seu peso (Kg): \33[1;32m'))
altura = float(input('\33[mInforme a sua altura (m): \33[1;32m'))

imc = peso / altura ** 2

if imc < 18.5:
    print(f'\n\33[mSeu IMC é \33[1;32m{imc:.1f}\33[m e você está abaixo do peso.')
elif imc < 25:
    print(f'\n\33[mSeu IMC é \33[1;32m{imc:.1f}\33[m e você está no peso ideal.')
elif imc < 30:
    print(f'\n\33[mSeu IMC é \33[1;32m{imc:.1f}\33[m e você está no sobrepeso.')
elif imc < 40:
    print(f'\n\33[mSeu IMC é \33[1;32m{imc:.1f}\33[m e você está obeso.')
else:
    print(f'\n\33[mSeu IMC é \33[1;32m{imc:.1f}\33[m e você tem obesidade mórbida.')