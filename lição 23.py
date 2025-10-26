frase = int(input('Digite um numero qualquer de 0 há 9999: '))
a = frase // 1000 % 10
b = frase // 100 % 10
c = frase // 10 % 10
d = frase // 1 % 10
print(' milhar {}\n centena {}\n dezena {}\n unidade {}'.format(a, b, c, d)) 