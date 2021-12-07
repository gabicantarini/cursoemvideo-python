#Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem
#no final de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

#Resolução Gabriela
#REVER EXERÍCIO, ESTÁ ERRADO!!!!!!!!!!!!!!!!!

#n1 = float(input("Primeira nota: "))
#n2 = float(input("Segunda nota: "))
#media = (n1 + n2) /2
#if media < 5:
#    print("REPROVADO!")
#elif media >= 5 and media <= 7:
#    print("RECUPERAÇÃO!")
#elif media >= 7:
#    print("APROVADO!")
#else:
#    print("Comando Inválido.")
#print(f"Sua média é {media}.")


#Resolução Guanabara


n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) /2
print((f"Tirando {n1} e {n2}, a média do aluno é {media}."))
if 7 > media >= 5:
    print("O aluno está em RECUPERAÇÃO!")
elif media < 5:
    print("O aluno está REPROVADO!")
elif media >= 7:
    print("O aluno está APROVADO!")

