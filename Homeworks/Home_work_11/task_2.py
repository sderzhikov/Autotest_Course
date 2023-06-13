# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# Создание экземпляра веб-драйвера
driver = webdriver.Chrome()

# Переход на страницу авторизации
driver.get("https://fix-online.sbis.ru/")
driver.maximize_window()
time.sleep(2)
# Ввод логина и пароля
login_input = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
time.sleep(2)
login_input.send_keys("Убадмин")
time.sleep(2)
# Нажатие на кнопку "Войти"
login_button = driver.find_element(By.CSS_SELECTOR, '.auth-AdaptiveLoginForm__loginButtonImage')
login_button.click()
time.sleep(2)
password_input = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
password_input.send_keys("й1ц2у3к4е5н6")
time.sleep(2)
# Нажатие на кнопку "Войти"
login_button = driver.find_element(By.CSS_SELECTOR, '.auth-AdaptiveLoginForm__loginButtonImage')
login_button.click()
time.sleep(5)

# Находим и кликаем на пункт аккордеона с текстом "Контакты"
accordion_items = driver.find_elements(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]')
for item in accordion_items:
    if "Контакты" in item.text:
        actions = ActionChains(driver)
        actions.click(item).click(item).perform()
        break
time.sleep(5)
# Нажатие на кнопку создания нового сообщения
create_message_button = driver.find_element(By.CSS_SELECTOR, '.controls-Button__icon.icon-RoundPlus')
create_message_button.click()
time.sleep(2)
# Ввод получателя сообщения
receiver_input = driver.find_element(By.CSS_SELECTOR, '[name="ws-input_2023-06-13"]')
receiver_input.clear()
receiver_input.send_keys("Админ Всея")
time.sleep(2)
# Выбор получателя сообщения
# Находим все элементы с классом "controls-Scroll-containerBase_userContent"
user_element = driver.find_element(By.CSS_SELECTOR, '.person-BaseInfo')
user_element.click()
time.sleep(2)
# Ввод текста сообщения
message_input = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
time.sleep(2)
message_input.send_keys("Как же я устал, Боже....")
time.sleep(2)
# Отправка сообщения
send_button = driver.find_element(By.CSS_SELECTOR, '.icon-BtArrow')
send_button.click()
time.sleep(2)
# Поиск сообщения в списке
# Находим все элементы с классом msg-dialogs-item_unread и текстом "Как же я устал, Боже"
message_elements = driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item_unread')

# Перебираем найденные элементы
for message_element in message_elements:
    # Проверяем текст сообщения
    if "Как же я устал, Боже" in message_element.text:
        # Выполняем наведение на элемент
        ActionChains(driver).move_to_element(message_element).perform()

        # Выполняем клик правой кнопкой мыши
        ActionChains(driver).context_click(message_element).perform()

        # Прерываем цикл, так как нашли нужное сообщение
        break

# Проверяем, видима ли кнопка "Перенести в удалённые"
move_to_trash_button = driver.find_element(By.CSS_SELECTOR, '.icon-Erase')
move_to_trash_button.click()


# Закрытие браузера
driver.quit()