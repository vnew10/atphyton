a = input('enter a: ')
b = input('enter b: ')
c = input('enter c: ')

a = float(a)
b = float(b)
c = float(c)

if a == b:
    print('a=b')
elif a == c:
    print('a=c')
elif b == c:
    print('b=c')
else:
    print('all numbers are different')
