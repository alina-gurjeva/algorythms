# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# Согласно примечаниям в лекции, умножение не обязательно

from collections import deque


def test_hex(func):  # все эти оборачивания в листы только из-за этого странного условия, что числа должны храниться так
    tests = [(list('A12'), list('B12')),
             (list('666A'), list('666B')),
             (list('EF7'), list('CB9')),
             (list('123A'), list('7B')),
             (list('0'), list('16')),
             (list('FFFF'),list('FFFFF')),
             (list('A2'), list('C4F'))

             ]
    answers = [list('1524'), list('CCD5'), list('1BB0'), list('12B5'), list('16'), list('10FFFE'), list('CF1')]
    for i in range(len(tests)):
        assert func(*tests[i]) == answers[i],\
            f'Ошибка {tests[i]}: {func(*tests[i])} != {answers[i]}'
    print('all tests ok!')


def _is_empty(x: iter):
    return len(x) == 0


# 0 1 2 3 4 5 6 7 8 9 A B C D E F
def sum_hex(hex_a: list, hex_b: list):
    hex_string = '0123456789ABCDEF'
    answer = deque()
    first_hex = deque()
    second_hex = deque()
    first_hex.extend(hex_a)
    second_hex.extend(hex_b)
    in_mind = 0

    while not _is_empty(first_hex) and not _is_empty(second_hex):
        s1, s2 = first_hex.pop(), second_hex.pop()
        s1_pos = hex_string.find(s1)
        s2_pos = hex_string.find(s2) + in_mind
        sum_pos = s1_pos + s2_pos
        in_mind = 0
        if sum_pos > 15:
            in_mind += 1
            sum_pos -= 16
        answer.appendleft(hex_string[sum_pos])

    if not _is_empty(first_hex):
        rest_hex = first_hex
    elif not _is_empty(second_hex):
        rest_hex = second_hex
    else:
        rest_hex = None

    if rest_hex is not None:
        while not _is_empty(rest_hex):
            rest_elem = rest_hex.pop()
            ind = hex_string.find(rest_elem) + in_mind
            in_mind = 0
            if ind > 15:
                in_mind += 1
                ind -= 16
            answer.appendleft(hex_string[ind])
    if in_mind:
        answer.appendleft('1')
    return list(answer)


# test_hex(sum_hex)  # проверка

first_num = list(input('Введите 1е 16-ричное число: '))
second_num = list(input('Введите 2е 16-ричное число: '))

print(sum_hex(first_num, second_num))
