import random
import time

print('qual operação você deseja fazer')
print('1 adição')
print('2 subtração')
operação = input()
num1 = input('diga um número ')
num2 = input('diga outro número ')

num3 = int(num1) + int(num2) + 2
num4 = int(num1) + int(num2) - 2

num5 = int(num1) - int(num2) + 2
num6 = int(num1) - int(num2) - 2

mais = [num3, num4]
resultado = random.choice(mais)

menos = [num5, num6]
resultado2 = random.choice(menos)

if operação == '1':
    print(f'{num1}+{num2}={resultado}')
if operação == '2':
    print(f'{num1}-{num2}={resultado2}')

time.sleep(2)
print('(observação:o calculo está errado em mais ou menos dois)')
time.sleep(10)
