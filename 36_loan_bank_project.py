#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

#Resolução Gabriela
#vcasa = float(input("Qual o valor da casa? R$ "))
#scomprador = float(input("Qual o seu salário? R$  "))
#meses = (prazo*12)
#vmensal = (vcasa/meses)
#sparcial = ((scomprador*30)/100)
#if vmensal <= sparcial:
#    print("Parabéns, seu empréstimo foi aprovado!")
#else:
#    print("Desculpe, seu empréstimo não foi aprovado.")

#Resolução Guanabara
casa = float(input("Valor da casa: R$ "))
salário = float(input("Salário do comprador: R$  "))
anos = int(input("Quantos anos de financiamento?  "))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print(f"Para comprar uma casa de R$ {casa:.2f} em {anos}")
print(f"a prestação será de R$ {prestação:.2f}")
if prestação <= mínimo:
    print("Empréstimo pode ser CONCEDIDO!")
else:
    print("Empréstimo NEGADO!.")
