# Задание 1: Дано одно число - сторона квадрата.
# Напишите программу, которая рассчитает три значения: периметр квадрата, площадь квадрата и диагональ квадрата.

side = float(input("Введите длину стороны квадрата: "))  # Получаем на вход длину стороны квадрата
perimeter = 4 * side  # Рассчитываем периметр
area = side ** 2  # Рассчитываем площадь
diagonal = side * 2 ** 0.5  # Рассчитываем диагональ
print(f'''Площадь квадрата: {area}\nПериметр квадрата: {perimeter}\nДиагональ квадрата: {diagonal}''')
