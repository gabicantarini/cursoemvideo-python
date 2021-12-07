#Ex.44
#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
#de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20% de juros


#Resolução Gabriela
pn = float(input("Qual o preço normal do produto? R$ "))
dc = (pn * 10) /100
avc = (pn * 5) /100
duas = pn
tres = (pn * 20) /100
#print(f"Para pagamento a vista em dinheiro ou no cheque, você terá 10% de desconto R$ {dc} e pagará R$ {pn-dc:.2f} no seu produto.")
#print(f"Para pagamento a vista no cartão, você terá 10% de desconto R$ {avc} e pagará R$ {pn-avc:.2f} no seu produto.")
#print(f"Para pagamento em até 2x no cartão, você não terá desconto e pagará R$ {duas} no seu produto.")
#print(f"Para pagamento em 3x ou mais no cartão, você terá um acréscimo de R$ {tres} e pagará R$ {pn+tres:.2f} no seu produto.")

print("Nós temos as seguintes opções de pagamento: ")
print("[1] À vista dinheiro/cheque")
print("[2] À vista no cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")

pgto = int(input("Qual a sua forma de pagamento? "))

if pgto == 1:
    print(f"Para pagamento a vista em dinheiro ou no cheque, você terá 10% de desconto R$ {dc} e pagará R$ {pn-dc:.2f} no seu produto.")
elif pgto == 2:
    print(f"Para pagamento a vista no cartão, você terá 10% de desconto R$ {avc} e pagará R$ {pn - avc:.2f} no seu produto.")
elif pgto == 3:
    print(f"Para pagamento em até 2x no cartão, você não terá desconto e pagará R$ {duas} no seu produto.")
elif pgto == 4:
    print(f"Para pagamento em 3x ou mais no cartão, você terá um acréscimo de R$ {tres} e pagará R$ {pn + tres:.2f} no seu produto.")
else:
    print("Opção Inválida!!!")


#Resolução Guanabara
print(f'{"LOJAS GUANABARA":=^40}')
preço = float(input("Preço das compras: R$ "))
print("""FORMAS DE PAGAMENTO: 
[1] À vista dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
opção = int(input("Qual é a opção? "))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f"Sua compra será parcelada em 2X de R$ {parcela:.2f}.")
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print(f"Sua compra será parcelada em {totparc} X {parcela:.2f} COM JUROS.")
else:
    total = preço
    print("OPÇÃO INVÁLIDA de pagamento. Tente novamente!")
print(f"Sua compra de R$ {preço:.2f} vai custar R$ {total:.2f} no final. ")
