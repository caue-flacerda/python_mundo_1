pa = float(input('Digite quantos KM você irá percorrer: '))
if pa <= 200:
    print("O preço da viagem ficou {:.2f}R$".format(pa * 0.50))
else:
    print("O preço da viagem ficou {:.2f}R$".format(pa * 0.45))
