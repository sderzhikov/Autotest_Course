# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# Создание экземпляра веб-драйвера
driver = webdriver.Chrome()

# Переход на страницу авторизации
driver.get("https://fix-online.sbis.ru/page/dialogs")
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
time.sleep(10)

# Нажатие на кнопку создания нового сообщения
create_message_button = driver.find_element(By.CSS_SELECTOR, '.controls-Button__icon.icon-RoundPlus')
create_message_button.click()
time.sleep(5)
# Ввод получателя сообщения
receiver_input = driver.find_element(By.CSS_SELECTOR, '[data-qa="addressee-selector-root"] input')
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
time_sent = datetime.datetime.now()
time.sleep(8)
# Поиск сообщения в списке
# Находим все элементы с классом msg-dialogs-item_unread и текстом "Как же я устал, Боже"
message_elements = driver.find_elements(By.CSS_SELECTOR, '.controls-ListView__itemContent:has(.msg-dialogs-item_unread)')

# Перебираем найденные элементы
for message_element in message_elements:
    # Проверяем текст сообщения
    if time_sent.strftime("%H:%M") in message_element.find_element(By.CSS_SELECTOR, "[data-qa='msg-entity-date']").text \
            and "Как же я устал, Боже" in message_element.text:
        # Выполняем наведение на элемент
        ActionChains(driver).move_to_element(message_element).perform()
        time.sleep(1)
        # Прерываем цикл, так как нашли нужное сообщение
        break


erase = driver.find_element(By.XPATH, '//div[@class="controls-itemActionsV__wrapper"]//i[contains(@class, "icon-Erase")]')
erase.click()
time.sleep(8)
for message_element in message_elements:
    # Проверяем текст сообщения
    assert time_sent.strftime("%H:%M") in message_element.find_element(By.CSS_SELECTOR, "[data-qa='msg-entity-date']").text
    assert "Как же я устал, Боже" in message_element.text

# Закрытие браузера
driver.quit()