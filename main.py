from square_number import ListSquareNumber
from sample import Sample

try:
    list_n_number = list(map(int, input('Введите целые числа через пробел: ').split()))
except ValueError as v:
    print('Ошибка ввода')
    exit()
try:
    degree = float(input('В какую степень возвести числа? '))
except ValueError as v:
    print('Неправильный ввод')
    exit()
answer = ListSquareNumber(list_n_number, degree)
print(answer.list_square_number())



# try:
#     list_number = list(map(int, input('Введите целые числа через пробел: ').split()))
# except ValueError as v:
#     print('Ошибка ввода')
#     exit()
# try:
#     choice = int(input('Какие числа вывести, выберете вариант (цирфу):'
#                    '\n 1: Четные'
#                    '\n 2: Нечетные'
#                    '\n 3: Простые \n'))
# except ValueError as v:
#     print('Неправильно выбрана операция')
#     exit()
# if not 1 <= choice <= 3:
#     print('Неправильно выбрана операция')
#     exit()
# answer = Sample(list_number, choice)
# print(answer.select_list())
