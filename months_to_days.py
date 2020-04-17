month = input('Enter a Month: ')
if month.lower() == 'february':
    print('28 or 29 days')
elif (month.lower() == 'april'
    or month.lower() == 'june'
    or month.lower() == 'september'
    or month.lower() == 'november'):
        print('30 days')
else:
    print('31 days')
