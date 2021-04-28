# 4. Определить, какое число в массиве встречается чаще всего.

import random

len_array_nums = 10
min_array_nums = 0
max_array_nums = 2

array_nums = [random.randint(min_array_nums, max_array_nums) for _ in range(len_array_nums)]


unique_nums = list(set(array_nums))  # т.к. важен порядок элементов
k_nums = [0 for i in range(len(unique_nums))]

for i in range(len(unique_nums)):
    k = array_nums.count(unique_nums[i])
    k_nums[i] = k

max_elem_array = k_nums[0]
max_index = 0
for ind, element in enumerate(k_nums):
    if element > max_elem_array:
        max_elem_array = element
        max_index = ind


print(unique_nums[max_index])
print(f'Исходный массив: {array_nums}')
