"""Exercício 06.

Área do Círculo
Desenvolva um programa que calcule e mostre a área de um círculo a partir do raio
fornecido.
Fórmulas:
    a = π*r²
    π ≈ 3.14
"""
raio = int(input("digite o tamanho do raio: "))
π = float("3.14")
area = raio **2 * π 

print(area)