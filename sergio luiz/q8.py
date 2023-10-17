#Faça um programa para contar quantas vogais existem em uma palavra. Utilize a condicional IF dentro do laço FOR.
alfabeto = "abcdefghijklmnopqrsxz"
quantidade = 0

for letra in alfabeto:
    if letra not in "aeiou":
        print(f"Consoantes {letra}")
        