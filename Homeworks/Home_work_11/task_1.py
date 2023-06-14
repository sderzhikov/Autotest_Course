# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


# Создание экземпляра веб-драйвера
driver = webdriver.Chrome()

# Переход на https://sbis.ru/
driver.get("https://sbis.ru/")

# Разворот окна
driver.maximize_window()

# Переход в раздел "Контакты"
driver.find_element(By.LINK_TEXT, "Контакты").click()
time.sleep(2)

# Нахождение и клик на баннере "Тензор"
banner = driver.find_element(By.CSS_SELECTOR, "a[href='https://tensor.ru/']")
banner.click()

# Переключение на новую вкладку
driver.switch_to.window(driver.window_handles[-1])

# Находим блок "Свои люди" и кнопку "Подробнее" в нем
block = driver.find_element(By.CSS_SELECTOR, "div.tensor_ru-Index__block4-content.tensor_ru-Index__card")
button = block.find_element(By.CSS_SELECTOR, "a.tensor_ru-link.tensor_ru-Index__link[href='/about']")

# Скроллим до блока
actions = ActionChains(driver)
actions.move_to_element(button).perform()

# Закрываем тупую плашку, перекрывающую кнопку "Подробнее"
close_stupid_shit = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-CookieAgreement__close")
close_stupid_shit.click()
time.sleep(2)

# Нажимаем кнопку "Подробнее" в блоке "Свои люди"
button.click()
time.sleep(2)
expected_url = "https://tensor.ru/about"
current_url = driver.current_url

# Проверяем, что мы попали на нужную страницу
assert current_url == expected_url, "Не то"

# Закрытие веб-драйвера
driver.quit()
