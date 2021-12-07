#Faça um programa que leia o ano de um nascimento de um jovem e informe, de acordo com a sua idade:
# -Se ele ainda vai se alistar ao serviço militar.
# -Se é a hora de se alistar.
# -Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

#Pesquisa documentation
#date = datetime.date.today()
#year = date.strftime("%Y")
#print(f"Current Year -> {year}")

#Resolução Gabriela
from datetime import date
ano = int(input("Digite o ano que você nasceu: "))
date = date.today().year
idade = date - ano
resto = 18 - idade
dif = idade - 18
if idade < 18:
    print(f"Ainda não é a sua hora. Você deverá se alistar em {resto} anos.")
elif idade > 18:
    print(f"Você perdeu o prazo para se alistar. Já passaram {dif}")
else:
    print("Já é hor ade se alistar!")




