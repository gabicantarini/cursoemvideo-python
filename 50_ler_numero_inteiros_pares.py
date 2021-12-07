#Desenvolva um programqa que leia 6 números inteiros e mostre a soma somente daqueles que foram pares.
# Se o valor digitado for ímpar, desconsidere-o.


soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f"Digite o {c}º valor: "))
    if num % 2 ==0:
        cont = cont + 1 #ou cont += 1
        soma = soma + num #ou soma += num
print(f"Você informou {cont} números e a soma foi {soma}")

