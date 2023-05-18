# Создание виртуального окружения
# Создайте файл task4.py c кодом:
import sys
import os

if sys.prefix == sys.base_prefix:
    print('Вы не активировали виртуальное окружение')
    print(f'Текущее окружение {sys.base_prefix}')
    os.system("pip list")
else:
    print(f'Вы используете виртуальное окружение {sys.prefix}')
    os.system("pip list")

# Создайте виртуальное окружение.
# Запустите task4.py
# Сохраните скрин вывода результата. У вас должна быть выведена строка "Вы используете виртуальное окружение ..."
# Установите selenium версии 4.8.0 в виртуальное окружение.
# Запустите task4.py и сохраните скрин вывода.
# Деактивируйте витруальное окружение, сменив на нативный интерпретатор Python (по умолчанию у вас 3.11)
# Повторите запуск кода и сохраните скрин вывода результата в консоль.  У вас должна быть выведена строка:
# "Вы не активировали виртуальное окружение
# Текущее окружение ..."

# В качестве решения пришлите скрины выводов:
# Первый скрин после запуска кода с активированным виртуальным окружением.
# Второй скрин списка установленных библиотек в виртуальном окружении с selenium==4.8.0.
# Третий скрин после запуска кода с деактивированным виртуальным окружением.