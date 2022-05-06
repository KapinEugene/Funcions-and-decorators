def decorate_method(method):
    from timeit import default_timer

    def wrapper(self, *args, **kwargs):
        start = default_timer()
        conclusion = method(self, *args, **kwargs)
        end = default_timer()
        print('Время выполнения: {:f} секунд.'.format(end - start))
        return conclusion

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
