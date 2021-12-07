#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. (Número
# primo só é dividido por 1 e por ele mesmo)



n = int(input("digite um número: "))
tot=0
for c in range(1, n +1):
    if n % c == 0:
        print("\33[33m", end = ' ')
        tot += 1
    else:
        print("\033[31m", end = '')
    print(f"{c}", end = ' ')
print(f"\n\033[mO número {n} foi divisível {tot} vezes.")
if tot == 2:
    print("E por isso ele é primo!")
else:
    print("E por isso ele não é primo!")



n = int(input("digite um número: "))
mult=0

for count in range(2,n):
    if (n % count == 0):
        print("Múltiplo de",count)
        mult += 1

if(mult==0):
    print("É primo")
else:
    print("Tem",mult," múltiplos acima de 2 e abaixo de",n)