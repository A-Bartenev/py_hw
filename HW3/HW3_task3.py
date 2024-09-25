"""Функция проверки на простое число.
Простые числа – это такие числа, которые делятся на себя и на единицу.
Пример:
17 -> True
20 -> False
23 -> True"""
number=23
def check_prime_numbers(number_check:int):
    count_remainder_division=0
    for i in range(number_check+1):
        try:
            if number_check%i==0:
                count_remainder_division+=1
            else:
                pass
        except ZeroDivisionError:
            pass
    if count_remainder_division>2:
        return False
    else:
        return True

print(check_prime_numbers(number))