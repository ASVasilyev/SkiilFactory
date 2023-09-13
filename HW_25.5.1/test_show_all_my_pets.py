from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""Тест проверяет все ли мои питомцы присутствуют на экране. 
Для этого сравниваем количество питомцев в таблице на экране со значением счётчика питомцев в моём профиле"""


def test_show_all_my_pets(driver):
    WebDriverWait(driver, 11).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), 'PetFriends')
    )

    driver.find_element(By.CSS_SELECTOR, 'a.nav-link[href="/my_pets"]').click()  # переходим на вкладку Мои Питомцы

    driver.implicitly_wait(10)

    all_my_pets = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')  # Находим всех питомцев в таблице

    assert len(all_my_pets) > 0     # проверяем что список своих питомцев не пуст

    my_info = driver.find_element(By.CSS_SELECTOR, '.\\.col-sm-4.left')  # Находим элемент слева, где указано количество питомцев
    my_info_text = my_info.text.split("\n")
    print(my_info_text)
    count_pets = my_info_text[1]  # Получаем строку Питомцы: количество
    parts = count_pets.split(": ")
    number_of_pets = int(parts[1])  # Получаем количество питомцев

    assert len(all_my_pets) == number_of_pets
