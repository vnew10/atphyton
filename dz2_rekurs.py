def cut_sq(a, b, count=0):
    if a > b:
        a, b = b, a

    if a == b:
        print(f'the last sq {a}x{a}')
        count += 1
        print('the number of sq = ', count)
        return

    print(f'the sq {a}x{a}')
    count += 1
    cut_sq(a, b-a, count)


a = int(input('enter a: '))
b = int(input('enter b: '))
if a < 0 or b < 0:
    print('incorrect input')
else:
    cut_sq(a, b)
