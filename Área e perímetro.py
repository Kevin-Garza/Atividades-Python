# Exercício 5: Faça um programa em que o usuário digita o raio de um círculo em m e o programa retorna no console a área do círculo em m² e o perímetro em m.

import math

def calcular_area_e_perimetro(raio):
    area = math.pi * raio ** 2
    perimetro = 2 * math.pi * raio
    return area, perimetro
raio = float(input("Insira o raio da circunferência que deseja calcular a área e o perímetro em metros: "))
area, perimetro = calcular_area_e_perimetro(raio)
print(f"A área da circunferência é {area:.2f}m².")
print(f"O perímetro da circunferêcia é {perimetro:.2f}m")