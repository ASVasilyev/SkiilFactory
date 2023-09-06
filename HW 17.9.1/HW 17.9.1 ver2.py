"""Программа получает на вход массив неупорядоченных целых чисел и число(элемент поиска). После чего программа устанавливает
 номер позиции элемента в списке, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу."""


def binary_search(array, element, left, right):
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
sort_array = sort(my_array)

print(sort_array)

if my_element < sort_array[0]:
    print('Введенный элемент меньше первого в списке.')
elif my_element == sort_array[0]:
    print('Введенный элемент равен первому в списке.')
elif my_element > sort_array[len(sort_array) - 1]:
    print('Введенный элемент больше последнего в списке.')
else:
    print(f'Номер позиции: {binary_search(sort_array, my_element, 0, len(sort_array) - 1)}')
