'''Написать функцию, которая будет перводит снейк_кейс в КэмелКейс и наоборот. Функция сама определяет - какой формат ей передали.
Можно добавить ключевой аргумент, который будет принудительно возвращать один из форматов.
Пример:
otus_course -> OtusCourse
PythonIsTheBest -> python_is_the_best '''


string_input = "OtusCourse"
def camel_snake_convert(string):
    if '_' in string:
        string = string.split('_')
        for _ in range(len(string)):
            string[_]=string[_].capitalize()
        string = ''.join(string)
        print(string)
    else:
        result = ''
        for i in string:
            if i.isupper():
                result+='_'+i.lower()
            else:
                result+=i
        result=result.lstrip('_')
        print(result)
        return

camel_snake_convert(string_input)
