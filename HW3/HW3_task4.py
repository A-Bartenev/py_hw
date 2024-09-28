'''Пользователь в бесконечном цикле вводит данные пользователей: имя, затем фамилию, возраст и ID.
Ввод продолжается до тех пор, пока не будет введено пустое поле.
Пользователи заносятся в словарь, где ключ это ID пользователя, а остальные данные записываются в виде кортежа.
Так же программа должна проверять, что имя и фамилия состоят только из символов и начинаются с большой буквы, если н
е с большой, то заменяет на большую, возраст должен быть числом от 18 до 60, ID - целое число, дополненное до 8
знаков незначащими нолями, ID должен быть уникальным
Дополнительно написать функцию, которая будет выводить полученный словарь в виде таблицы


савелий пипин 43 13
иван1 пупа 23 15
иван пупа2 23 15
иван пупа 16 15
иван пупа 61 15
иван пупа 60 15
иван пупа 60 15
иван пупа 60 15ыа
иван пупа 60 16
'''

dict_id={}
temp_list=[]
def check_and_capitalize_name_last_name(temp_list):
     if temp_list[0].isalpha() and temp_list[1].isalpha():
         temp_list[0]=temp_list[0].capitalize()
         temp_list[1]=temp_list[1].capitalize()
         return True
     else:
         print ('В имени и фамилии на может быть цифр и спец символов, повторите ввод: ')
def check_age(temp_list):
    temp_list[2]=int(temp_list[2])
    if 18<=temp_list[2]<=60:
        return True
    else:
        print( 'Возраст должен быть числом от 18 до 60, повторите ввод:')
def print_result(dict_id):
    for key, value in dict_id.items():
        print(f"{key}",end='    ')
        for i in value:
            print(i, end='    ')
        print()
def check_id_and_add_dict(temp_list,dict_id):
    if len(temp_list[3])>8:
        print ('Длина ID не более 8 знаков, повторите ввод: ')
    elif temp_list[3].isdigit()==False:
        print ('ID может быть только целым числом, повторите попытку:')
    else:
        id='0'*(8-len(temp_list[3]))+temp_list[3]
        if id in dict_id:
            print ("Такой ID уже есть, введите уникальный ID:")
            return
        else:
            dict_id[id]=(temp_list[0],temp_list[1],temp_list[2])

while True:
    string_input =input()
    if string_input== str(''):
        break
    elif string_input == str('итог'):
        print_result(dict_id)
    else:
        temp_list = string_input.split(' ')
        if check_and_capitalize_name_last_name(temp_list)==True:
            if check_age(temp_list)==True:
                check_id_and_add_dict(temp_list,dict_id)


