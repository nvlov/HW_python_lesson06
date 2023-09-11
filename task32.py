# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_intervals(arr, min_val, max_val):
    intervals = []
    for i in range(len(arr)):
        if arr[i] >= min_val and arr[i] <= max_val:
            intervals.append((i, arr[i]))
    return intervals

# Пример использования функции
arr = [-1, 22, 88, -9, 0, 5, 10, 15, 20, 25]
min_val = -1
max_val = 20

intervals = find_intervals(arr, min_val, max_val)
print("Интервалы элементов списка", arr, "которые соответствуют заданным минимальным и максимальным значениям:", intervals)