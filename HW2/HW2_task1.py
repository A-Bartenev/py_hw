"""Пользователь вводит целое число, программа складывает все цифры числа, с полученным числом - то же самое
 и так до тех пор, пока не получится однозначное число.
Пример:
545 -> 5
12345 -> 6"""

vvod = input('Введите число:')
vvod = int(vvod[::-1])


def func_summa(vvod):
    summa = 0
    while vvod != 0:
        summa += vvod % 10
        vvod = vvod // 10
    return summa


result = func_summa(vvod)
while result > 9:
    result = func_summa(result)

print(result)
