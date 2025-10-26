frase = str(input("Digite o nome da sua cidade: ")).strip().upper()
a = frase.split()
c = 'SANTO' in a[0]
print('Começa com ,Santo, a sua cidade? ',c)
