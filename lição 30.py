num =str((input('Digite um número inteiro: '))).strip()
par = ['0', '2', '4', '6', '8']
b = ' '.join(num)
c = b.split()
print(b)
print(c)
if c[-1] in par:
    print('Esse número {} é par'.format(num))
else:
    print('Esse número {} é impar'.format(num))
