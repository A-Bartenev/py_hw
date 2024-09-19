"""Написать упрощенную версию алгоритма RLE. Алгоритм RLE объединяет подряд идущие символы
в коэффициент и символ.
Пример:
aaabbbbccccc -> 3a4b5c
asssdddsssddd -> 1a3s3d3s3d
abcba -> 1a1b1c1b1a"""
string_input="abcba"
result=''
count = 1
while len(string_input)!=0:
    try:
        if string_input[0]==string_input[1]:
            count+=1
        elif string_input[0]!=string_input[1]:
            if count==0:
                count=1
                result += str(count) + string_input[0]
            else:
                result += str(count) + string_input[0]
                count=1
        string_input = string_input[1:]
    except IndexError:
        result += str(count) + string_input[0]
        break


print(result)