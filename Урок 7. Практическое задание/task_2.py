"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import uniform


def merge_sort(input_array):
    if len(input_array) < 2:
        return input_array
    else:
        middle = int(len(input_array) / 2)
        left_part = merge_sort(input_array[:middle])
        right_part = merge_sort(input_array[middle:])
        return merge(left_part, right_part)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


arr = [uniform(0, 50) for _ in range(10)]
sorted_array = merge_sort(arr)
print(f"Исходный - {arr}")
print(f"Отсортированный - {sorted_array}")
