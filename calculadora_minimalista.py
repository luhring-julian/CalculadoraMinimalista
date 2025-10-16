#=========================================
# Calculadora de Bolso Minimalista (V1)
# Desenvolvida para reforçar os conhecimentos adquiritos no Bootcamp LuizaLabs
# Usa apenas input, conversão e operadores aritméticos
#=========================================

print("=== CALCULADORA DE BOLSO MINIMALISTA ===\n")

numero_1 = input("Digite o primeiro número: ")
numero_1 = float(numero_1)

numero_2 = input("Digite o segundo número: ")
numero_2 = float(numero_2)

# Operações aritméticas
soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
produto = numero_1 * numero_2
divisao = numero_1 / numero_2

#Resultado na tela
print(f"{numero_1} + {numero_2} = {soma}")
print(f"{numero_1} - {numero_2} = {subtracao}")
print(f"{numero_1} * {numero_2} = {produto}")
print(f"{numero_1} / {numero_2} = {divisao}")

print("\nCálculo concluído com sucesso!")