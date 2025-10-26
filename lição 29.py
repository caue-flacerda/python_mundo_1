velocidade = int(input("Entre com sua velocidade: "))
limite = 80
if velocidade > limite:
    total = (velocidade - limite) * 7
    print("Você ultrapassou o limite de velocidade de 80km/h. Sua multa ficará no valor de {}R$".format(total))
else:
    print("Tenha uma boa viagem!")
