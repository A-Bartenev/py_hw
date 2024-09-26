'''Написать функцию проверяющую валидность введенной даты.
Пример:
29.02.2000 -> True
29.02.2001 -> False
31.04.1962 -> False'''


'''
предобработка даты
'''
date='31.04.1962'
date = date.split('.')
for i in range(len(date)):
    date[i]=int(date[i])
day,month,year=date


def year_visocosn(year):
    '''
    Функция проверяет високосный год или нет
    :param year: год
    :return: True/False
    '''
    if year % 400==0 and year % 100 != 0:
        return True
    elif year % 4 == 0:
        return True
    else:
        return False
def check_date(day, month, year):
    '''
    Функция проверяет валидность даты.
    :param day: день
    :param month: месяц
    :param year: год
    :return: True/False
    '''
    if month<0 and 12<month and year<0:
        return False

    elif month==2:
        if year_visocosn(year)==True and 0<day<=29:
            return True
        elif year_visocosn(year)==False and 0<day<=28:
            return True
        else:
            return False

    elif month <=7:
        if month%2==0 and 0<day<=30:
            return True
        elif month%2==1 and 0<day<=31:
            return True
        else:
            return False

    elif month >=8:
        if month % 2 == 0 and 0 < day <= 31:
            return True
        elif month % 2 == 1 and 0 < day <= 30:
            return True
        else:
            return False

print(check_date(day, month, year))
help(check_date)