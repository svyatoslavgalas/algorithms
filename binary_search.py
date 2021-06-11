def binary_search(array: list, item: int) -> None:
    """
    Получаем на вход отсортированную последовательность(список) и элемент, который будем искать(item),
    в цикле берем число из середины списка:
    если число(guess) равно числу(item), которое мы ищем, возвращаем индекс числа,
    если число(guess) больше числа(item), которое мы ищем, то список сокращается вдвое от начала до середины,
    иначе список сокращается с середины и до конца
    Возвращаем None, если число не найдено.
    :param array: последовательность(список) в котором ищем элемент.
    :param item: число которое мы ищем в списке.
    :return: возвращаем индекс числа, или None, если число не найдено.
    """
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


test_list = [4, 8, 15, 16, 23, 42]

print(binary_search(test_list, 8))
print(binary_search(test_list, 23))
print(binary_search(test_list, 15))


def binary_search_max_num(array: list) -> int:
    """
    Задачка на примере бинарного поиска
    Дан отсортированный список, который был смещен на n кол-во,
    надо найти максимальное число.
    Например: [4, 8, 15, 16, 23, 42] -> [16, 23, 42, 4, 8, 15]
    """
    high = len(array) - 1

    while True:
        """Ищем середину"""
        mid = high // 2
        if len(array) == 2:
            """Если длинна элементов равна двум, то возвращаем больший"""
            if array[0] > array[-1]:
                return array[0]
            else:
                return array[-1]
        elif array[mid] > array[-1]:
            """Если центральный элемент больше последнего, то мы берем правую часть списка"""
            array = array[mid:]
        elif array[-1] > array[mid] > array[0]:
            """Если элементы идут по порядку, то возвращаем последний элемент"""
            return array[-1]
        else:
            """Если нет, то берем левую часть списка"""
            array = array[:mid]


test_list = [16, 23, 42, 4, 8, 15]
print(binary_search_max_num(test_list))

test_list = [23, 42, 4, 8, 15, 16]
print(binary_search_max_num(test_list))

test_list = [42, 4, 8, 15, 16, 23]
print(binary_search_max_num(test_list))

test_list = [4, 8, 15, 16, 23, 42]
print(binary_search_max_num(test_list))


def binary_search_max_num_v_2(array: list) -> int:
    """
    Задачка на примере бинарного поиска
    Дан отсортированный список, который был смещен на n кол-во,
    надо найти максимальное число.
    Например: [4, 8, 15, 16, 23, 42] -> [16, 23, 42, 4, 8, 15]
    """
    high = len(array) - 1

    while True:
        """Ищем середину"""
        mid = high // 2
        if len(array) == 3:
            """Выбираем больший из трех элементов"""
            if array[0] > array[1] and array[0] > array[2]:
                return array[0]
            elif array[1] > array[2]:
                return array[1]
            else:
                return array[2]
        elif array[mid] > array[-1]:
            """Если центральный элемент больше последнего, то мы берем правую часть списка"""
            array = array[mid:]
        else:
            """Крайний правый элемент, добавляем в левую часть"""
            array = [array[-1]] + array[:mid]


test_list = [16, 23, 42, 4, 8, 15]
print(binary_search_max_num_v_2(test_list))

test_list = [23, 42, 4, 8, 15, 16]
print(binary_search_max_num_v_2(test_list))

test_list = [42, 4, 8, 15, 16, 23]
print(binary_search_max_num_v_2(test_list))

test_list = [4, 8, 15, 16, 23, 42]
print(binary_search_max_num_v_2(test_list))
