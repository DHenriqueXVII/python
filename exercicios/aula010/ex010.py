retas = [
    float(input('Informe o valor da 1ª reta: ')),
    float(input('Informe o valor da 2ª reta: ')),
    float(input('Informe o valor da 3ª reta: '))
]

if retas[0] + retas[1] > retas[2] and retas[1] + retas[2] > retas[0] and retas[0] + retas[2] > retas[1]:
    print('Os valores informados podem formar um triângulo!')
else:
    print('Os valores informados não podem formar um triângulo!')