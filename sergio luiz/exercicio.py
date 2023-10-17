#Faça um programa que pede para o usuáro inserir uma palavra e mostre na tela e se essa palavra contem a letra "A"

palavra = str(input("Digite uma palavra: ")).lower()

tem_a_letra_a = False
quantidade = 0

for letra in palavra:
   if letra == 'a':
       tem_a_letra_a = True
       quantidade = quantidade + 1

if tem_a_letra_a == True:      
    print(f"Sua palavra contém {quantidade} letras A")
else:
    print("Sua palavra não contém a letra A")
