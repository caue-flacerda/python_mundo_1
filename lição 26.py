frase = str(input("Digite algo: ")).strip().upper()
print("aparece {} vezes a letra 'a'".format(frase.count('A')))
print("A letra 'a' aparece pela primeira vez na posição {} ".format(frase.find('A')+1))
print("A letra 'a' apareceu pela última vez na posição {}".format(frase.rfind('A')+1))
