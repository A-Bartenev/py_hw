'''Шифр Цезаря. Пользователь вводит строку и ключ шифра, программа должна вывести зашифрованную строку
(со сдвигом по ключу). Сдвиг циклический.
Используем только латинский алфавит, пробелы не шифруются.
Пример:
Dog, 2 -> Fqi
Zak zak, 3 -> Cdn cdn
Python is the BEST, 5 -> Udymts nx ymj GJXY
'''

string_cipher = 'Zak zak' # исходная строка
lower_alph='abcdefghijklmnopqrstuvwxyz'
upper_alph ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
spec_char = f' *?/\|<>,.()[]{{}}\'\";:!@#$%^&'
shift = 3 # сдвиг
cipher_result=''

for i in string_cipher:
    if i in spec_char:# обрабатываем спецсимволы
         cipher_result+=i
    elif i.isupper():# проверяем верхний регистр
        if upper_alph.find(i)+shift > (len(upper_alph)-1):# проверям простой сдвиг или циклический
            shift_null=shift -((len(upper_alph))-upper_alph.find(i))# находим индекс с начала строки
            cipher_result += upper_alph[shift_null]
        else:# если сдвиг не циклический, находим индекс значения со сдвигом и добавляем в результат
            cipher_result+=upper_alph[upper_alph.find(i)+shift]
    elif i.islower(): # проверяем нижний регистр
        if lower_alph.find(i)+shift > (len(lower_alph)-1): # проверям простой сдвиг или циклический
            shift_null=shift -((len(lower_alph))-lower_alph.find(i))# находим индекс с начала строки
            cipher_result += lower_alph[shift_null]
        else:# если сдвиг не циклический, находим индекс значения со сдвигом и добавляем в результат
            cipher_result+=lower_alph[lower_alph.find(i)+shift]
print(cipher_result)