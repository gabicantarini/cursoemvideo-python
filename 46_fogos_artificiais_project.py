#Ex.46
#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

#i = int(input("Ínicio: "))
#f = int(input("Fim: "))
#p = int(input("Passo: "))
#for c in range(i, f+6, p):
#    print(c)
#print("FIM")

#Resolução Gabriela
from time import sleep
print("10")
sleep (1)
print("09")
sleep (1)
print("08")
sleep (1)
print("07")
sleep (1)
print("06")
sleep (1)
print("05")
sleep (1)
print("04")
sleep (1)
print("03")
sleep (1)
print("02")
sleep (1)
print("01")
sleep (1)
print("0")
sleep (1)
print("\U0001F386")

#Resolução Guanabara
from time import sleep
for cont in range(10, 0, -1):
    print(cont)
    sleep(0.5)
print("\U0001F386")




