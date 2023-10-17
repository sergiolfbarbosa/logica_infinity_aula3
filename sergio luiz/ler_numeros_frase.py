#Faça um programa que pede ao usuário para digitar uma frase, percorra essa frase e mostre na tela um print de cada número dentre dessa frase.print

frase = str(input("Digite uma frase:" ))

for ler_numero_frase in frase:
    if ler_numero_frase in "0123456789":
        print(f"Números {ler_numero_frase}") 