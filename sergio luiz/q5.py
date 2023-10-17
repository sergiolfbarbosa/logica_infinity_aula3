#Faça um programa para calcular a média de uma lista de números.

print("Digite 10 números")
soma = 0

for i in range(1, 11):
       numero = float(input(f"Digite o, {i}º número: "))
       soma = soma + numero

print("A soma é", soma, "e a média é", soma / 10)