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
        self.__list_n_number = list_n_number
        self.degree = degree

    def generator(self):
        list_prime_numbers = []
        for k in self.__list_n_number:
            counter = 0
            for j in range(2, k+1):
                if k % j == 0:
                    counter += 1
            if counter == 1:
                list_prime_numbers.append(k)
        yield list_prime_numbers

    @decorate_method
    def list_square_number(self):
        list_number_squared = []
        for i in self.__list_n_number:
            list_number_squared.append(int(i**self.degree))
        return list_number_squared
