import random
number = random.randint(1, 36)
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

print(f'The spin resulted in {number}...')
print(f'Pay {number}')

if number in red:
    print('Pay Red')
else:
    print('Pay Black')

if number % 2 == 0:
    print('Pay Even')
else:
    print('Pay Odd')

if number <= 18:
    print('Pay 1 to 18')
else:
    print('Pay 19 to 36')