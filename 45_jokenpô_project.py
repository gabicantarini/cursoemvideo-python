#Crie um programa que faça o computador jogar Jokenpô com você. Jokenpô = Pedra, Papel e Tesoura
#Possibilidades:
#pedra e papel = papel OK
#tesoura e papel = tesoura OK
#pedra e tesoura = pedra OK

#Falta conf. para aceitar letras maiusculas e minusculas e espaços

#Solução Gabriela
#from random import choice
#n1 = str(input("Pedra, Papel ou Tesoura? "))
#lista = ["Pedra", "Papel", "Tesoura"]
#n2 = choice(lista)
#print(f"Pedra, Papel ou Tesoura? {n2}")
#if n1 == n2:
#    print("Deu empate, jogue novamente!")
#elif n1 == "Pedra" and n2 == "Papel" or n1 == "Papel" and n2 == "Tesoura" or n1 == "Tesoura" and n2 == "Pedra":
#    print("O computador ganhou!")
#elif n2 == "Pedra" and n1 == "Papel" or n2 == "Papel" and n1 == "Tesoura" or n2 == "Tesoura" and n1 == "Pedra":
#    print("Parabéns, você ganhou!")
#else:
#    print("inválido")


#Solução Guanabara
from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
print("""Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
jogador = int(input("Qual é a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)
print(f'{"-="*15}')
print(f"O computador escolheu {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print(f'{"-="*15}')
if computador == 0: #Compuatdro jogou Pedra
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador ==2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 1: #Compuatdro jogou Papel
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador ==2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVÁLIDA")
elif computador == 3: #Compuatdro jogou Tesoura
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador ==2:
        print("EMPATE")
    else:
        print("JOGADA INVÁLIDA")

