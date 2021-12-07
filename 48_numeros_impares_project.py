#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.



#Resolução Gabriela
soma = 0
cont = 0
for c in range(3,501,6):
    if c % 2:
        soma = soma + c
        cont = cont + 1
print(f"A soma de todos {cont} os valores solicitados é {soma}")


#Resolução Guanabara
soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        cont = cont + 1 #ou pode ser cont+=1
        soma = soma + c #ou pode ser soma+=c
print(f"A soma de todos {cont} os valores solicitados é {soma}")



