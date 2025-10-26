a = float(input("Entre com o primeiro segmento: "))
b = float(input("Entre com o segundo segmento: "))
c = float(input("Entre com o terceiro segmento: "))
maior = a
menor = a
meio = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if maior == a or maior == c and menor == a or menor == c:
    meio = b 
if maior == a or maior == b and menor == a or menor == c:
    meio = c
if meio + menor > maior:
    print("Esses segmentos formam um triângulo")
else: 
    print("Esses segmentos não formam um triângulo")