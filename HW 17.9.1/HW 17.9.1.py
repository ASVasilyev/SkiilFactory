"""Программа получает на вход массив неупорядоченных целых чисел и число(элемент поиска). После чего программа устанавливает
 номер позиции элемента в списке, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу."""


def binary_search(array, element, left, right):
    if element > array[right]:  # если элемент больше последнего в списке
        return f'Введенный элемент больше последнего в списке.'
    elif element < array[0]:  # если элемент меньше первого в списке.
        return f'Введенный элемент меньше первого в списке.'
    elif element == array[0]:  # если элемент равен первому в списке.
        return f'Введенный элемент равен первому в списке.'
    else:
        middle = (right + left) // 2  # находим середину

        if array[middle] == element:  # если элемент в середине,
            return middle - 1  # возвращаем этот индекс-1
        elif element < array[middle]:  # если элемент меньше элемента в середине
            if element > array[middle - 1]:  # если элемент больше, чем стоящий перед серединой
                return middle - 1  # возвращаем это индекс
            else:  # иначе продолжаем поиск в левой части
                return binary_search(array, element, left, middle - 1)
        else:  # иначе в правой
            return binary_search(array, element, middle + 1, right)


def sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array


my_array = list(map(int, str.split(input("Введите числа через пробел:"))))
my_element = int(input('Введите элемент для поиска позиции:'))

print(sort(my_array))

print(f'Номер позиции: {binary_search(sort(my_array), my_element, 0, len(sort(my_array)) - 1)}')
