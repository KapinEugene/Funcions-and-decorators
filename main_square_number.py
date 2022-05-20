from square_number import ListSquareNumber


list_numbers_with_condition = []
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
for k in list_n_number:
    if 100 <= k <= 1000:
        list_numbers_with_condition.append(k)
print(list_numbers_with_condition)
answer = ListSquareNumber(list_n_number, degree)
answer = answer.list_square_number()
generator_answer = ListSquareNumber(list_numbers_with_condition, degree)
print(answer)
for i in generator_answer.generator():
    print(i)
