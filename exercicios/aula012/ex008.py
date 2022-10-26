s1 = int(input('Primeiro seguimento: \33[1;32m'))
s2 = int(input('\33[mSegundo seguimento: \33[1;32m'))
s3 = int(input('\33[mTerceiro seguimento: \33[1;32m'))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    if s1 == s2 and s1 == s3 and s2 == s3:
        print('\n\33[mOs segmentos acima PODEM FORMAR um triângulo EQUILÁTERO.')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('\n\33[mOs segmentos acima PODEM FORMAR um triângulo ISÓSCELES.')
    else:
        print('\n\33[mOs segmentos acima PODEM FORMAR um triângulo ESCALENO.')
else:
    print('\n\33[mOs segmentos acima NÃO PODEM FORMAR um triângulo.')