"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
"""
import random
import math
import numpy as np

m = 5
N = 2 * m + 1
MIN = 0
MAX = 10
ARRAY = [random.uniform(MIN, MAX) for _ in range(N)]  # заполнен случайным образом


def test_median(func):
    test_arrays = [
        [0],
        [1, 1, 1],
        [-3, -2, -1],
        [0.1, 0.2, 0.3, 0.4, 0.5],
    ]
    for t in test_arrays:
        random.shuffle(t)
        assert np.median(t) == func(t), f'Error on {t}, {np.median(t)} != {func(t)}'
    print('all tests ok')


def median(arr: list):
    if not arr:
        return 'ERROR: zero array'
    l = len(arr)
    middle = math.ceil(l/2)
    potential_median_index = []
    median_indexes = []
    s = 0
    for i in range(l):
        x = arr[i]
        for j in range(l):
            if x < arr[j]:
                s += 1
                if s > middle:
                    break
        if s < middle:
            potential_median_index.append(i)
        s = 0
    s = 0
    for i in potential_median_index:
        x = arr[i]
        for j in range(l):
            if x > arr[j]:
                s += 1
                if s > middle:
                    break
        if s < middle:
            median_indexes.append(i)
        s = 0
    return arr[median_indexes[0]]


# test_median(median)

#  Найдите в массиве медиану
print('Медиана: ', median(ARRAY))
# для наглядности
print('Исходный отсортированный массив: ')
print(sorted(ARRAY))
