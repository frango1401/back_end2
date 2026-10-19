# Questão 1 - Controle de temperatura
# Peça ao usuário a temperatura atual de uma sala (número inteiro). Classifique-a em Frio (abaixo de 18),
# Agradável (de 18 até 26, inclusive) ou Quente (acima de 26).
# Identificador padronizado da temperatura: temp_sala_ref.
# Em seguida, informe se o ventilador deve ficar ligado (temperatura acima de 26) ou desligado (nos demais
# casos).
# Teste/Exemplo: Exemplos: 15 → Frio / ventilador desligado; 22 → Agradável / desligado; 29 → Quente / ligado.

ventilador = int(input("digite a temperatura atual da sala: "))

if ventilador < 18:
    print("esta frio ventilador desligado")
elif 18 <= ventilador <= 26:
    print("esta agradavel, ventilador desligado")
else:
    print("esta quente, ventilador ligado")
