# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

len_array_nums = 10
min_array_nums = -10
max_array_nums = 10

array_nums = [random.randint(min_array_nums, max_array_nums) for _ in range(len_array_nums)]

min_elem_array = array_nums[0]
min_index = 0
max_elem_array = array_nums[0]
max_index = 0
for ind, element in enumerate(array_nums):
    if element < min_elem_array:
        min_elem_array = element
        min_index = ind
    if element > max_elem_array:
        max_elem_array = element
        max_index = ind
print(f'До: {array_nums}')
array_nums[min_index], array_nums[max_index] = array_nums[max_index], array_nums[min_index]
print(f'После: {array_nums}')
