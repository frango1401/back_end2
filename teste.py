# frutas = ["maça", "melancia", "cereja", "bergamota", "goiaba"]
# fruta_fora = frutas.pop(0)
# print(frutas)
# print(fruta_fora)

# pessoa = {"nome": "adebenovaldo", "idade": 30, "cidade": "anta gorda"}
# print(pessoa["nome"])
# print(pessoa["idade"])
# print(pessoa["cidade"])

# pessoa = {"nome": "adebenovaldo", "idade": 30, "cidade": "anta gorda"}
# print(pessoa.get("endereço", "Endereço não cadastrado"))

# a = int(input("digite um numero: "))

# if a > 20:
#     print("maior que 20")
# elif a == 20:
#     print("igual a 20")
# else:
#     print("menor que vinte")

# contador = 1
# while contador < 4:
#     print(f"condição verdadeira. contador{contador}")
#     contador = contador + 1
# print("fim do programa")

# senha = input("digite a senha: ")
# while senha == "adebenovaldo":
#     print("senha invalida. tente novamente")
#     senha = input("digite a senha: ")
# print("senha correta")

# Questão 1 - Controle de temperatura
# Peça ao usuário a temperatura atual de uma sala (número inteiro). Classifique-a em Frio (abaixo de 18),
# Agradável (de 18 até 26, inclusive) ou Quente (acima de 26).

# ventilador = int(input("digite a temperatura atual da sala: "))

# if ventilador < 18:
#     print("esta frio ventilador desligado")
# elif 18 <= ventilador <= 26:
#     print("esta agradavel, ventilador desligado")
# else:
#     print("esta quente, ventilador ligado")

# Crie um programa com uma senha fixa, definida no próprio código. O usuário terá até 3 tentativas para
# digitá-la corretamente. Utilize while para controlar as tentativas.
# Identificador padronizado do contador: contador_acesso_ref.
# Se acertar, exiba Acesso permitido e encerre as tentativas; se esgotar as três tentativas sem acertar, exiba
# Acesso bloqueado. Não mostre a senha na tela durante a execução.
# Teste/Exemplo: Teste obrigatório: acertar na primeira tentativa, acertar na terceira e errar as três.

# senha_correta = "adebenovaldo"

# contador = 0
# while contador < 3:
#     senha_digitada = input("digite a senha: ")
#     contador += 1

#     if senha_digitada == senha_correta:
#         print("senha correta")
#         break
# else:
#     print("senha errada")

# Peça um número inteiro positivo N entre 1 e 20. Usando for e range(N), exiba os valores de 0 até N - 1, mas
# não mostre o número 3 quando ele aparecer.
# Identificador padronizado da variável de repetição: indice_exibicao_ref.
# Use continue para ignorar esse valor. Ao final, informe quantos números foram exibidos. Considere que o
# usuário digitará um N válido.
# Teste/Exemplo: Exemplo: N = 6 → exibe 0, 1, 2, 4, 5; quantidade exibida = 5.