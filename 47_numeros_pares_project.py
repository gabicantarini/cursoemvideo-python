#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

#Resolução correta só que mais extensa
#for cont in range(1,51):
#    if cont % 2 == 0:
#        print(cont, end=" ")


#Resolução Guanabara
#Para diminuir o número de laços faça:
# A lógica é vc começar a contar do 2 e já fazer a conta de 2 em 2.


for cont in range(2,51,2):
    if cont % 2 == 0:
        print(cont, end=" ")
print("ACABOU!")


# Obs: O programador bom chega no mesmo resultado dando menos trabalho para o computador