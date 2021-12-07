#Desenvolva um programa que leia o primeiro termo de uma PA (Progressão Aritimética).
# No final, mostre os 10 primeiros termos dessa progressão.



print(F'{"10 TERMOS DE UMA PA":=^40}')
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(c, end="\U000027A1|")
print("ACABOU!")

