#Лабораторная работа №1. Вариант 3.

RED = "\033[41m"
WHITE = "\033[47m"
BLUE = "\033[44m"
END = "\033[0m"


def flag():
    for i in range(12):
        if i < 5:
            print(f'{RED}{" " * 60}{END}')
        elif i < 10:
            print(f'{WHITE}{" " * 60}{END}')
        else:
            print(f'{BLUE}{" " * 60}{END}')


def pattern():
    repeats=6

    line1 = r"\ / " * repeats
    line2 = r" X  " * repeats
    line3 = r"/ \ " * repeats

    print(line1)
    print(line2)
    print(line3)


def graph():
    plot_list = [[0 for i in range(10)] for i in range(10)]
    result = [0 for i in range(10)]

    for i in range(10):
        result[i] = 2*i

    step = round(abs(result[0] - result[9]) / 9, 2)
    print(step)

    for i in range(10):
        for j in range(10):
            if j == 0:
                plot_list[i][j] = step * (8-i) + step

    for i in range(9):
        for j in range(10):
            if abs(plot_list[i][0] - result[9 - j]) < step:
                for k in range(9):
                    if 8 - k == j:
                        plot_list[i][k+1] = 1

    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += '\t' + str(int(plot_list[i][j])) + '\t'
            if plot_list[i][j] == 0:
                line += '--'
            if plot_list[i][j] == 1:
                line += '!!'
        print(line)
    print('\t0\t1 2 3 4 5 6 7 8 9')





def diag():
    file = open('Lab-1/sequence.txt', 'r')
    list = []
    for number in file:
        list.append(float(number))
    file.close()

    c_sum = 0
    n_sum = 0
    for i, n in enumerate(list, start=1):
        if i % 2 == 0:
            c_sum += abs(n)
        else:
            n_sum += abs(n)

    print(f"Сумма модулей чисел на нечётных позициях = {c_sum}")
    print(f"Сумма модулей чисел на чётных позициях  = {n_sum}")

    total = c_sum + n_sum
    c_percent = c_sum * 100.0 / total
    n_percent = n_sum * 100.0 / total

    width = 50

    c_len = int(c_percent * width / 100.0 + 0.5)
    n_len = int(n_percent * width / 100.0 + 0.5)

    print("Диаграмма процентного соотношения суммы модулей чисел:")

    print(f"Нечётные {c_percent:6.2f}% " + BLUE + " " * c_len + END)

    print(f"Чётные   {n_percent:6.2f}% " + RED + " " * n_len + END)


flag()
pattern()
graph()
diag()
