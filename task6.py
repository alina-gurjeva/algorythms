# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random


def guess_num(attempts, x):
    if attempts == 0:
        print(f'Игра окончена! Ответ: {x}')
        return
    guess = int(input('Введите число: '))
    if guess > x:
        print('Больше!')
        return guess_num(attempts - 1, x)
    if guess < x:
        print('Меньше!')
        return guess_num(attempts - 1, x)
    if guess == x:
        print("Угадал")
        return


x = random.randint(0, 100)
attempts = 10
guess_num(attempts, x)
