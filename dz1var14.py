def enter_age():
    while True:
        k = input('Введите возраст от 1 до 9: ')
        k = int(k)
        if k < 1 or k > 9:
            print('Неправильное значение')
            continue
        return k


def print_message(k, age):
    print(f'Мне {k} {age}')


k = enter_age()
if k == 1:
    print_message(k, 'год')
elif k in [2, 3, 4]:
    print_message(k, 'года')
else:
    print_message(k, 'лет')
