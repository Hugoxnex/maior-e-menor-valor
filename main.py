p1 = int(input(" Primeiro Valor "))
p2 = int(input(" Segundo Valor "))
p3 = int(input(" Terceiro Valor "))
# verificando menor valor 
menor = p1
if p2 < p1 and p2 < p3:
    menor = p2
if p3 < p1 and p3 < p2:
    menor = p3
# verificando maior valor
maior = p1 
if p2 > p1 and p2 > p3:
    maior = p2
if p3 > p1 and p3 > p2:
    maior = p3
print(" O menor valor digitado é {} ".format(menor))
print(" O maior valor digitado é {} ".format(maior))