## Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. 
# Каждое число вводится с новой строки.

a1 = int(input("Введите значение первого элемента: "))
d = int(input("Введите значение разности: "))
n = int(input("Введите количество элементов: "))

progression = []
for i in range(n):
    element = a1 + (i * d)
    progression.append(element)

print("Элементы арифметической прогрессии:")
for element in progression:
    print(element)
	