"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
"""
import random

N = 100
ARRAY = [random.randint(-100, 99) for _ in range(N)]


def test_reverse_sort(func):
    """
    Тест функции сортирующей по убыванию
    :param func:
    """
    arrays = [
        [3, 1, 2],
        [1, 1, 1],
        [1, 2, 3],
        [0],
        [1, 2, 7, 4]
    ]
    for ar in arrays:
        assert sorted(ar, reverse=True) == func(ar), f'Error on {ar}'
    print('all tests ok')


def bubble_sort_reverse(arr: list):
    """
    немного улучшенный алгоритм пузырьковой сортировки по убыванию
    :param arr:
    :return: sorted array
    """
    array = arr.copy()
    l = len(array)
    s = 0
    for _ in range(l):
        for i in range(l-1):
            if array[i] < array[i+1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                s += 1
        if s == 0:  # дальше можно не проверять т.к. не было замен на предыдущем витке
            break
        else:
            s = 0
    return array


# test_reverse_sort(bubble_sort_reverse)

print('Исходный массив: ')
print(ARRAY)
print('Отсортированный массив: ')
print(bubble_sort_reverse(ARRAY))


