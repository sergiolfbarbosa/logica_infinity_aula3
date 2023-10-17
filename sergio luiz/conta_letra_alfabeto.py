#Faça um programa que print todas as letra do alfabeto sem conter as vogais.
alfabeto = "abcdefghijklmnopqrsxz"

for letra in alfabeto:
    if letra not in "aeiou":
        print(f"Consoantes {letra}")
