import math
ângulo = float(input("Digite um ângulo: "))
seno = math.sin(math.radians(ângulo))
print("O ângulo de {} tem o seno de {:.2f}".format(ângulo, seno))
cos = math.cos(math.radians(ângulo))
print("O ângulo de {} tem o cosseno de {:.2f}".format(ângulo, cos))
tan = math.tan(math.radians(ângulo))
print("O ângulo de {} tem o tangente de {:.2f}".format(ângulo, tan))