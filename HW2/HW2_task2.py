'''Кинотеатр. Дан список списков, каждый вложенный список состоит из 1 и 0,
Количество вложенных списков - количество рядов. Пользователь вводит сколько билетов ему требуется.
 Программа должна найти ряд, где можно приобрести нужно количество билетов (места должны быть рядом).
 Если таких рядов несколько, то ближайший к экрану (ближайшим считается нулевой ряд).
 Ели таких мест нет, то вывести False
Пример:
[[0,1,1,0], [1, 0, 0, 0], [0,1,0,0]], 2 -> 1
[[0,1,1,0], [1, 0, 1, 0], [1,1,0,1]], 2 -> False'''

list_place_hall=[[0,1,1,0], [1, 0, 0, 0], [0,1,0,0]]
count_place=2
for i in list_place_hall:
    str_elem =  ''.join([str(j) for j in i])
    if '0'*count_place in str_elem:
        print(f'{list_place_hall},{count_place} --> {list_place_hall.index(i)}')
        break
else:
    print(f'{list_place_hall}, {count_place} --> False')
