#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# -O primeiro valor é maior
# -O segundo valor é maior
# -Não existe valor maior, os dois são iguais

#Resolução Gabriela = a do Guanabara
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite um número inteiro: "))
if n1 > n2:
    print("O primeiro valor é maior.")
elif n1 < n2:
    print("O segundo valor é maior.")
else:
    print("Não existe valor maior, os dois são iguais.")
