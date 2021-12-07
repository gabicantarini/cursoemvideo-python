#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Pesoa ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

#Resolução Gabriela
p = float(input("Qual o seu peso (KG)? "))
a = float(input("Qual a sua altura (M)? "))
imc = p / (a ** 2)
print(f"O seu IMC é {imc:.1f}.")
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 25 > imc >= 18.5:
    print("Você está no peso ideal.")
elif 30 > imc >= 25:
    print("Você está com sobrepeso.")
elif 40 > imc >= 30:
    print("Você está obeso.")
else:
    print("Você está com obesidade mórbida.")