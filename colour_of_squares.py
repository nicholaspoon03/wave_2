letters_str = 'abcdefgh'

position = input('Enter a valid position on the checkerboard: ')
letter = position[0].lower()
number = int(position[1])

begin_black = False

if letters_str.find(letter) % 2 == 0:
    begin_black = True

if begin_black and number % 2 != 0:
    print('black')
elif begin_black and number % 2 == 0:
    print('white')
elif not begin_black and number % 2 != 0:
    print('white')
else:
    print('black')