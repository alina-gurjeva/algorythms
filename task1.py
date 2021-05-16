"""
Согласно комментарию на лекции нужно выбрать одно любое задание из 2х.
"""

"""
Исходное задание звучало так:

1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

ИЗ ПОЯСНЕНИЯ НА ЛЕКЦИИ
в сумму не включать пустую строку и исходную строку целиком.

Также из пояснения на лекции выяснилось, что на самом деле мы ищем не количество подстрок.
А количество всех возможных перестановок подмножеств символов исходной строки, 
длина каждого подмножества от 1 символа до количества символов в строке включительно.
"""

"""
Из-за неоднозначности условия относительно пояснения на лекции, решений будет 2.
"""
from collections import Counter
from math import factorial
import itertools  # что не запрещено, то разрешено

N = 3
S = 'aba'  # or just input()

"""
1е решение. Если имелось в виду все же не подслова, 
а количество всех возможных перестановок всех подмножеств символов исходной строки,
исключая пустое подмножество и исходную строку.
"""


def test_counter(func):
    tests = ['aba', 'aaa', 'ab', 'a', 'abc']
    answers = [7, 2, 3, 0, 14]
    for i in range(len(tests)):
        t = tests[i]
        a = answers[i]
        res = func(t)
        assert res == a, f'Error on {t}: {res}!={a}'
    print('all tests ok')


"""
Пояснения к тесту:
'aba': a b ab ba aa aab baa
'aaa': a aa
'ab': a b ba
'a': -
'abc': a b c ab ac bc ba ca cb bac acb cba cab bca 

"""


def count_permutations(s: str, is_whole=False):
    """
    :param s: str
    :param is_whole: if s == S
    :return count of all permutations:
    """
    n = len(s)
    repeats = Counter(s)
    divisor = 1
    for v in repeats.values():
        divisor = divisor * factorial(v)
    k_permutations = factorial(n) / divisor
    if is_whole:
        k_permutations -= 1
    return int(k_permutations)


def count_combinations(s: str):
    len_s = len(s)
    k_all_permutations = 0
    cache = set()
    for k_letter in range(1, len_s):  # all excluding permutantions of whole S string
        combinations_k = itertools.combinations(s, k_letter)
        for next_comb in combinations_k:
            sorted_string = ''.join(sorted(next_comb))
            if hash(sorted_string) in cache:
                pass
            else:
                # строго говоря, в set() итак хэши, hash() здесь не нужен. здесь только из-за формулировки задания
                cache.add(hash(sorted_string))
                k_permutations = count_permutations(sorted_string)
                k_all_permutations += k_permutations
    k_permutations = count_permutations(s, is_whole=True)
    k_all_permutations += k_permutations
    return k_all_permutations


# test_counter(count_combinations)
print(count_combinations(S))

"""
2е решение. Если имелись в виду именно подстроки.

Считаем количество подстрок, опять же НЕ включая пустую строку и исходную строку.
"""


def test_counter_substrings(func):
    tests = ['aba', 'aaa', 'ab', 'a', 'abc', 'abcd', 'addd']
    answers = [4, 2, 2, 0, 5, 9, 6]
    for i in range(len(tests)):
        t = tests[i]
        a = answers[i]
        res = func(t)
        assert res == a, f'Error on {t}: {res}!={a}'
    print('all tests ok')


"""
Пояснения к тесту:
'aba': a b ab ba
'aaa': a aa
'ab': a b
'a': -
'abc': a b c ab bc
'abcd': a b c d ab bc cd abc bcd
'addd': a d ad dd add ddd
"""


def count_substrings(s: str):
    len_s = len(s)
    cache = set()
    for k_letters in range(1, len_s):
        for i in range(len_s):
            j = i + k_letters
            if j > len_s:
                break
            # строго говоря, в set() итак хэши, hash() здесь не нужен. Здесь только из-за формулировки задания
            substring = hash(s[i:j])
            cache.add(substring)
    return len(cache)


# test_counter_substrings(count_substrings)
print(count_substrings(S))
