#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Ex: APOS A SOPA - A SACADA DA CASA - A TORRE DA DERROTA - OLOBO AMA O BOLO - ANOTARAM A DATA DA MARATONA


#Resolução Guanabara
frase = str(input("Digite um frase: ")).strip() .upper()
#.sprip() para eliminar os espaços antes e depois e .upper() para deixar tudo em maiúsculo
palavras = frase = frase.split() #split para separar em lista
#palavras é um tratamento de string que separa a frase em palavras
junto = ''.join(palavras) #juntar tudo numa string só
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
#fizemos a lista do for para ter o inverso da frase toda
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo.")


#Solução: https://www.mygreatlearning.com/blog/palindrome-in-python/
def check_palindrome(string):
    length = len(string)
    first = -0
    last = length -1
    status = 1
    while(first<last):
           if(string[first]==string[last]):
               first=first+1
               last=last-1
           else:
               status = 0
               break
    return int(status)
string = input("Digite uma frase: ").strip() .upper()
status= check_palindrome(string)
if(status):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo. Tente novamente!")
