a = float(input("Entre com o primeiro segmento: "))
b = float(input("Entre com o segundo segmento: "))
c = float(input("Entre com o terceiro segmento: "))
if a < b + c and b < c + a and c < b + a:
    print("Esses segmentos formam um triângulo")
else: print("Esses segmentos não formam um triângulo")
