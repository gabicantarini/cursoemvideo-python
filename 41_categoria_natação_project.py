#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 25 anos: SÊNIOR
#Acima: MASTER


#Resolvido por Gabriela
#from datetime import date
#atual = date.today().year
#nascimento = int(input("Ano de nascimento: "))
#idade = atual - nascimento
#print(f"O atleta tem {idade} anos.")
#if idade <= 9:
#    print("Classificação: MIRIM")
#elif 9 < idade <= 14:
#    print("Classificação: INFANTIL")
#elif 14 < idade <= 19:
#    print("Classificação: JUNIOR")
#elif 19 < idade <= 25:
#   print("Classificação: SÊNIOR")
#else:
#    print("Classificação: MASTER")


#Resolvido por Guanabara
from datetime import date
atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento
print(f"O atleta tem {idade} anos.")
if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JUNIOR")
elif idade <= 25:
   print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")