from generator import Generator


try:
    bot_line = int(input())
    top_line = int(input())
except ValueError as v:
    print('Ошибка ввода')
    exit()
generator_answer = Generator(bot_line, top_line)
for i in generator_answer.generator():
    print(i)


