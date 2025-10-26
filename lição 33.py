n1 = int(input('Entre com a primeira nota: '))
n2 = int(input('Entre com a segunda: '))
n3 = int(input('Entre com a terceira: '))
menor = n1
maior = n1
if n1 > n2 and n3 > n2:
    menor = n2
if n1 > n3 and n2 > n3:
    menor = n3
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print("O valor maior é: {} e o menor: é {}".format(maior, menor))
