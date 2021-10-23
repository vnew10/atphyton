import random

A = []
n = input('Введите размер списка n: ')
n = int(n)

for i in range(n):
    x = random.randint(0, 99)
    A.append(x)

print('Начальный список:', A)

new_A = []
del_index = 0
del_items_count = 0

while del_index < n:
    A.pop(del_index - del_items_count)
    del_index += 7
    del_items_count += 1

print('Список после удаления элементов с индексами кратными 7:', A)