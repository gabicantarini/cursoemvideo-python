#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora
#utilizando um laço for.




#Resolução Guanabara
num = int(input("Digite um número para ver sua tabuada: "))
for c in range(1,11):
    print(f"{num} x {c:.2f} = {num*c:.2f}")

#Resolução site Python
tabuada=int(input("Tabuada do numero: "))
for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )

