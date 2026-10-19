# Questão 2 - Tentativas de acesso
# Crie um programa com uma senha fixa, definida no próprio código. O usuário terá até 3 tentativas para
# digitá-la corretamente. Utilize while para controlar as tentativas.
# Identificador padronizado do contador: contador_acesso_ref.
# Se acertar, exiba Acesso permitido e encerre as tentativas; se esgotar as três tentativas sem acertar, exiba
# Acesso bloqueado. Não mostre a senha na tela durante a execução.
# Teste/Exemplo: Teste obrigatório: acertar na primeira tentativa, acertar na terceira e errar as três.

senha_correta = "adebenovaldo"

contador = 0
while contador < 3:
    senha_digitada = input("digite a senha: ")
    contador += 1

    if senha_digitada == senha_correta:
        print("senha correta")
        break
else:
    print("senha errada")
