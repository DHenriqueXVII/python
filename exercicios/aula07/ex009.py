altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))

def calcularArea(altura, largura):
    area = altura * largura
    tinta = area / 2
    return [area, tinta]

print(f'A area da parede é {calcularArea(altura, largura)[0]} M² e você precisará de {calcularArea(altura, largura)[1]:.2f} litros de tinta para pinta-la por completo')