import random
import time
num1 = input('diga um número?')
num2 = input('diga outro número')

num3 = int(num1) + int(num2) + 2
num4 = int(num1) + int(num2) - 2

opcoes = [num3, num4]
resultado = random.choice(opcoes)
print(resultado)

time.sleep(2)
print('(observação:o calculo está errado em mais ou menos dois)')
