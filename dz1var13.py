k = input('How many mushrooms have you collected? ')
last_number = k[-1]
last_number = int(last_number)
if last_number == 1:
    print('Мы нашли', k, 'гриб')
elif last_number == 2 or last_number == 3 or last_number == 4:
    print('Мы нашли', k, 'гриба')
else:
    print('Мы нашли', k, 'грибов')
