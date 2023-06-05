# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

with open('test_file/task_3.txt', 'r') as file:
    purchases = file.read().strip().split('\n\n')  # Разделяем покупки по пустым строкам и удаляем лишние пробелы

# Преобразуем строки покупок в список списков чисел
purchases = [[int(price) for price in purchase.split()] for purchase in purchases]

# Считаем сумму каждой покупки
purchase_sums = [sum(purchase) for purchase in purchases]

# Сортируем покупки по убыванию суммы и выбираем три самые дорогие
three_most_expensive_purchases = sorted(purchase_sums, reverse=True)[:3]

# Вычисляем общую сумму трех самых дорогих покупок
total_sum = sum(three_most_expensive_purchases)

print(total_sum)

assert total_sum == 202346
