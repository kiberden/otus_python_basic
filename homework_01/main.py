"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*number_list: list) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number**2 for number in number_list]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number: int) -> bool:
    """
    Метод проверяет число на простоту
    """
    if number < 2:
        return False

    for index in range(2, number // 2 + 1):
        if number % index == 0:
            return False
    return True


def filter_numbers(*number_list: list) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    number_list, type_filter = number_list
    filter_map = {
        ODD: lambda number: number % 2 != 0,
        EVEN: lambda number: number % 2 == 0,
        PRIME: lambda number: is_prime(number)
    }

    return list(filter(filter_map[type_filter], number_list))
