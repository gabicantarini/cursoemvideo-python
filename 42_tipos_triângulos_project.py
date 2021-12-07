#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isóceles: dois lados iguais
# - Escaleno: todos os lados diferentes


#Resolvido Gabriela
n1 = float(input("Primeiro Segmento: "))
n2 = float(input("Segundo Segmento: "))
n3 = float(input("Terceiro Segmento: "))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("Os segmentos acima podem formar um triângulo!")
    if n1 == n2 and n1 == n3 and n2 == n3:
        print("Os segmentos PODEM FORMAR um triângulo EQUILÁTERO")
    elif n1 != n2 != n3 != n1:
        print("Os segmentos PODEM FORMAR um triângulo ESCALENO")
    elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1:
        print("Os segmentos PODEM FORMAR um triângulo ISÓCELES")
else:
    print("Não formam um Trinângulo.")


#Resolvido Guanabara
r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float(input("Terceiro Segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima podem formar um triângulo ", end="")
    if r1 == r2 == r3:
        print("EQUILÁTERO")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISÓCELES")
else:
    print("Os segmentos acima não podem formar um Trinângulo.")