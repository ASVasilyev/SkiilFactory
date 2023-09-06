def binary_search(array, element, left, right):
    # if left > right:  # если левая граница превысила правую,
    #     return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle - 1  # возвращаем этот индекс-1
    elif element < array[middle]:  # если элемент меньше элемента в середине
        if element > array[middle-1]:  # если элемент больше, чем стоящий перед серединой
            return middle - 1  # возвращаем это индекс
        else:  # иначе продолжаем поиск в левой части
            return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

def sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx-1] > x:
            array[idx] = array[idx-1]
            idx -= 1
        array[idx] = x
    return array

array = list(map(int, str.split(input("Введите числа через пробел:"))))
element = int(input('Введите элемент для вставки:'))


print(sort(array))

print(binary_search(sort(array), element, 0, len(sort(array))-1))
