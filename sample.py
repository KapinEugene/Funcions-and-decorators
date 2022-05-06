def decorate_method(method):
    import time

    def wrapper(self, *args, **kwargs):
        start = time.time()
        new_rez = method(self, *args, **kwargs)
        end = time.time()
        print('Время выполнения: {:2f} секунд.'.format(end - start))
        return new_rez
    return wrapper


class Sample(object):
    def __init__(self, list_number, choice):
        self.list_number = list_number
        self.choice = choice

    @decorate_method
    def select_list(self):
        new_list_number = []
        if self.choice == 1:
            for i in self.list_number:
                if i % 2 == 0:
                    new_list_number.append(i)
            return new_list_number
        if self.choice == 2:
            for i in self.list_number:
                if i % 2 != 0:
                    new_list_number.append(i)
            return new_list_number
        if self.choice == 3:
            for i in self.list_number:
                if i > 1:
                    number_of_divisors = 0
                    for j in range(1, i+1):
                        if i % j == 0:
                            number_of_divisors += 1
                    if number_of_divisors == 2:
                        new_list_number.append(i)
            return new_list_number
