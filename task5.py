# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

len_array_nums = 10
min_array_nums = -10
max_array_nums = 10

array_nums = [random.randint(min_array_nums, max_array_nums) for _ in range(len_array_nums)]


max_neg_el = None
pos = 0
for ind, element in enumerate(array_nums):
    if element < 0:
        if max_neg_el is None:
            max_neg_el = element
        else:
            if element > max_neg_el:
                max_neg_el = element
                pos = ind
if max_neg_el is None:
    print('Отрицательных элементов нет')
else:
    print(f'Элемент: {max_neg_el}, позиция: {pos}')
    print(f'Исходный массив: {array_nums}')

