cash = float(input("Entre com seu salário: R$"))
if cash > 1250:
    print("Seu salário novo é: R${:.2f}".format((cash * 0.1)+ cash))
else: 
    print("Seu salário novo é: R${:.2f}".format((cash * 0.15)+ cash))
