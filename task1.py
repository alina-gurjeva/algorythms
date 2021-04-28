"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

# Решение через массивы:
for num in range(2, 10):
    nums_2_99 = [i for i in range(2, 100) if i % num == 0]
    print(f'Для числа {num} кратных чисел: {len(nums_2_99)}')

print('\n---------------------------------------------------\n')

# Альтернативное решение:
for num in range(2, 10):
    print(f'Для числа {num} кратных чисел: {99//num}')
