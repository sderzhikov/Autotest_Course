import os

path = "C:\\Users\\aa.sderzhikov\\Downloads\\photo_2023-05-03_09-52-02.jpg"

file_name = os.path.splitext(os.path.basename(path))[0]  # Используем функцию `splitext` модуля `os.path`,
# чтобы получить имя файла без расширения
# Используем функцию `splitdrive` того же модуля, чтобы получить название диска и корневую папку
disk_name = os.path.splitdrive(path)[0]
root_folder = os.path.splitdrive(path)[1].split(os.sep)[1]

print("Имя файла:", file_name)
print("Имя диска:", disk_name)
print("Корневая папка:", root_folder)
