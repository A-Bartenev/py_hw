"""
Пользователь вводит длину и ширину плитки шоколада, а также размер куска, который хочет отломить,
программа должна вычислить - можно ли совершить подобный разлом или нет, если учесть, что ломать можно только по прямой

Пример:

3, 4, 6 -> True
5, 7, 8 -> False
4, 5, 12 -> True"""


a, b, kusok = map(int, input().split(','))

if (kusok%a==0 and b>kusok//a) or (kusok%b==0 and a>kusok//b):
    print('True')
else:
    print('False')