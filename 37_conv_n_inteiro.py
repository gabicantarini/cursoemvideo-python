#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário - 2 para octal - 3 para hexadecimal (se digitar um será convertido pra binário, etc..)

#Resolução Gabriela
#import math
#n = int(input("Digite um número: "))
#print("""Qual base de conversão você prefere?
# 1 - Binário
# 2 - Octal
# 3 - Hexadecimal""")
#opção = int(input("Sua opção é: "))
#if opção == 1:
#    print(f"Seu número em binário é {bin(n)}")
#elif opção == 2:
#    print(f"Seu número em octal é {oct(n)}")
#elif opção == 3:
#    print(f"Seu número em hexadecimal é: {hex(n)}")
#else:
#    print(f"Número não reconhecido, tente novamente!")

#Resolução GUanabara
#[2:] usar para retirar os dois primeiros caracteres do resultado
#ele não importou math

n = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal""")
opção = int(input("Sua opção: "))
if opção == 1:
    print(f"O {n} convertido para BINÁRIO é igual a {bin(n)[2:]}")
elif opção == 2:
    print(f"O {n} convertido para OCTAL é igual a {oct(n)[2:]}")
elif opção == 3:
    print(f"O {n} convertido para HEXADECIMAL é igual a {hex(n)[2:]}")
else:
   print(f"Opção inválida. Tente novamente!")
