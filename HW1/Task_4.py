'''Пользователь вводит целое положительное число, программа должна вернуть строку в виде римского числа

Пример:

3 -> III
15 -> XV
234 -> CCXXXIV'''

roman_numbers = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
arabic=int(input('Введите число: '))
roman = ''
for letter, value in roman_numbers.items():
    while arabic >= value:
        roman += letter
        arabic -= value
print(roman)