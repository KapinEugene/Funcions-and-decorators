from square_number import ListSquareNumber


try:
    list_n_number = list(map(int, input('Введите целые числа через пробел: ').split()))
except ValueError as v:
    print('Ошибка ввода')
    exit()
if len(list_n_number) == 0:
    print('Вы ничего не ввели')
    exit()
try:
    degree = float(input('В какую степень возвести числа? '))
except ValueError as v:
    print('Неправильный ввод')
    exit()
answer = ListSquareNumber(list_n_number, degree)
print(answer.list_square_number())
