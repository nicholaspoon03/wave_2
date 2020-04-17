import math

a = int(input('A Value of Quadratic [A cannot be 0]: '))
b = int(input('B Value of Quadratic: '))
c = int(input('C Value of Quadratic: '))

discriminant = (b**2)-(4*a*c)
if discriminant > 0:
    print('2 solutions')
    print(f'x = {(-b+math.sqrt(discriminant))/(2*a)}')
    print(f'x = {(-b-math.sqrt(discriminant))/(2*a)}')
elif discriminant < 0:
    print('no solution')
else:
    print('1 solution')
    print(f'x = {(-b+math.sqrt(discriminant))/(2*a)}')