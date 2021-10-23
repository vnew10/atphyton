m = input('enter m: ')
n = input('enter n: ')
p = input('enter p: ')

m = float(m)
n = float(n)
p = float(p)

count = 0
if m < 0:
    count += 1
if n < 0:
    count += 1
if p < 0:
    count += 1

print('there are', count, 'negative numbers')
