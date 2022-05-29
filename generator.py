class Generator(object):
    def __init__(self, bot_line, top_line):
        self.__bot_line = bot_line
        self.__top_line = top_line

    def generator(self):
        list_prime_numbers = []
        for i in range(self.__bot_line, self.__top_line + 1):
            counter = 0
            for j in range(2, i + 1):
                if i % j == 0:
                    counter += 1
            if counter == 1:
                list_prime_numbers.append(i)
        yield list_prime_numbers
