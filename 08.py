"""Exercício 04.

Média das Notas
Faça um programa que peça quatro notas bimestrais e apresente a média delas.
"""

notas = []
notas.append(float(input("Digite a 1ª nota: ")))
notas.append(float(input("Digite a 2ª nota: ")))
notas.append(float(input("Digite a 3ª nota: ")))
notas.append(float(input("Digite a 4ª nota: ")))

media = sum(notas) / len(notas)

print(f"A média das notas é {media:.2f}")
