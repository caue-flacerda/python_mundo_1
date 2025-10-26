import random
print("O jogo consiste na máquina escolher um número de 1 a 5. Caso você acerte o número que a máquina escolheu, você ganha.")
m = input('Escolha um número de 1 a 5: ')
lista = [1 , 2, 3, 4, 5]
n = str(random.choice(lista))
if m == n:
    print('Parabéns! Você ganhou o jogo!')
else: 
    print('Você perdeu!')
print('{}'.format(n))
