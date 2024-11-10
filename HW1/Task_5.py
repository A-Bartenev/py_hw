n = input("Введите число: ")
try:
    float(n)
    print(n,'--> True')
except ValueError:
    print(n,'--> False')
