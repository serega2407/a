#Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
#элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: a
#n = a1 + (n-1) * d.
#Каждое число вводится с новой строки.


a1, d, n = int(input("Введите число: ")), int(input("Введите число: ")), int(input("Введите число: "))
progressive = [a1 + (i - 1) * d for i in range(1, n + 1)]
print(*progressive)