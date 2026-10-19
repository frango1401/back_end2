"""Exercício 02.

Cadastro de Usuário e Senha
Desenvolva um programa que receba um nome de usuário e sua senha.
O sistema deve validar se a senha é diferente do nome do usuário.
Caso seja igual, uma mensagem de erro deve ser exibida e as informações solicitadas
novamente até que sejam válidas.
"""
nome = input("digite o nome: ")
senha = input("digite a senha: ")

while nome == senha:
    print("Erro: A senha não pode ser igual ao nome do usuario")
    nome = input("digite o nome: ")
    senha = input("digite a senha: ")

print("Cadastro realizado: ")