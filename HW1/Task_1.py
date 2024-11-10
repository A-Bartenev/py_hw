"""Описание/Пошаговая инструкция выполнения домашнего задания:
Пользователь вводит пятизначное число. Программа должна зеркально отразить центральные три цифры. Первая и последняя остаются на местах.
Пример:
23456 -> 25436
30789 -> 38709"""
while True:
    string_input=input('Введите число: ')
    if len(string_input)!=5  or  string_input.isdigit()==False:
        print("5 знаков, только цифры, попробуйте еще раз: ")
        continue
    else:
        string_input=string_input[:1]+string_input[-2]+string_input[2]+string_input[1]+string_input[-1]
        print(string_input)
        break