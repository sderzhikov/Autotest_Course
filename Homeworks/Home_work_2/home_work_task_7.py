# Даны две строки из неповторяющихся символов:
# Первая строка длиной в три символа
# Вторая точно содержит символы первой строки в любом порядке
# Напишите программу, не используя циклы и условия, которая находит срез минимальной длины во второй строке
# (который будет содержать все символы первой строки)

string_1 = input("Введите первую строку из трех символов:", )
string_2 = input("Введите вторую строку, содержищую символы первой строки в любом порядке(без повторяющихся):", )
first_elem = string_2.find(string_1[0])
second_elem = string_2.find(string_1[1])
third_elem = string_2.find(string_1[2])
substring = string_2[min(first_elem, second_elem, third_elem):max(first_elem, second_elem, third_elem)+1]
print(substring)
