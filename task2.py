"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random

N = 10
ARRAY = []
i = 0
while i < N:
    x = random.uniform(0, 50)  # согласно документации, random.uniform включает обе границы
    if x == 50:
        continue
    else:
        ARRAY.append(x)
        i += 1


def test_sort(func):
    """
    Тест функции сортирующей по возрастанию
    :param func:
    """
    arrays = [
        [3, 1, 2],
        [1, 1, 1],
        [1, 2, 3],
        [0],
        [1, 2, 7, 4],
        [5, 4],
        [1, 1, 2, 2, 3, 1],
        [-7, -9, 0]
    ]
    for ar in arrays:
        assert sorted(ar) == func(ar), f'Error on {ar}'
    print('all tests ok')


def merge_sorting(arr):
    array = arr.copy()

    def _sort(array_):
        if len(array_) < 2:
            return array_
        else:
            mid = int(len(array_) / 2)
            left = _sort(array_[:mid])
            right = _sort(array_[mid:])
            return _merge(left, right)

    def _merge(ar1, ar2):
        result = []
        i, j = 0, 0
        while i < len(ar1) and j < len(ar2):
            if ar1[i] < ar2[j]:
                result.append(ar1[i])
                i += 1
            else:
                result.append(ar2[j])
                j += 1
        while i < len(ar1):
            result.append(ar1[i])
            i += 1
        while j < len(ar2):
            result.append(ar2[j])
            j += 1
        return result

    return _sort(array)


# test_sort(merge_sorting)

print('Исходный массив: ')
print(ARRAY)
print('Отсортированный массив: ')
print(merge_sorting(ARRAY))

