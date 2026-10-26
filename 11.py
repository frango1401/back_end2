"""Exercício 03.

Soma de Três Números
Elabore um programa que contenha uma função necessitando de três argumentos numéricos e
que retorne a soma desses três argumentos.
"""

def somar_tres_numeros(a, b, c):
    return a + b + c

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

resultado = somar_tres_numeros(num1, num2, num3)

print(f"A soma dos três números é: {resultado}")
