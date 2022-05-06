def decorate_method(method):
    import time

    def wrapper(self, *args, **kwargs):
        start = time.time()
        new_rez = method(self, *args, **kwargs)
        end = time.time()
        print('Время выполнения: {:2f} секунд.'.format(end - start))
        return new_rez
    return wrapper


class ListSquareNumber(object):
    def __init__(self, list_n_number, degree):
        self.list_n_number = list_n_number
        self.degree = degree

    @decorate_method
    def list_square_number(self):
        list_number_squared = []
        for i in self.list_n_number:
            list_number_squared.append(i**self.degree)
        return list_number_squared
