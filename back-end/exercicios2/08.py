"""Exercício 08.

Cálculo de Salário
Elabore um programa que calcule o salário mensal de uma pessoa, com base nas horas
trabalhadas por mês e no valor por hora.
"""
horas_trabalhadas = int(input("digite suas horas trabalhadas por mês: "))
valor_horas = int(input("digite o valos por horas trabalhadas: "))
salario_mensal = horas_trabalhadas * valor_horas * 30

print(salario_mensal)