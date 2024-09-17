"""Табель успеваемости. Пользователь в бесконечном цикле (пока не будет введена пустая строка) вводит строки вида:
 'название предмета' 'фамилия ученика' 'оценка'. После окончания ввода программа выводит в консоль Название предмета,
 далее список учеников и все их оценки в виде таблицы

Математика Иванов 5
Математика Иванов 4
Литература Иванов 3
Математика Петров 5
Литература Сидоров 3
Литература Петров 5
Литература Иванов 4
Математика Сидоров 3
Математика Петров 5

Математика
Иванов 5 4
Петров 5 5
Сидоров 3

Литература
Ивванов 3 4
Сидоров 3
Петров 5"""

rating_list=list()
lesson = set()
student = set()
while True:
    string_input =input()
    if string_input== str(''):
        break
    else:
        string_input = string_input.split(' ')
        rating_list.append(string_input)
for i in rating_list:# наполняю множество предметов и учеников
    for j in i:
        lesson.add(i[0])
        student.add(i[1])

list_lesson=list(lesson)
list_student = list (student)

for i in list_lesson:
    print()
    print(i)
    for s in list_student:
        print(s, end=' ')
        for rating in rating_list:
            if rating[0]==i and rating[1]==s:
                print(rating[2], end=' ')
        print()