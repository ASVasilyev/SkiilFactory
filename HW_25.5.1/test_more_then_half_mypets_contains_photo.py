from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""Тест проверяет, что как минимум у половины моих питомцев добавлено фото"""


def test_show_all_my_pets(driver):
    WebDriverWait(driver, 11).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), 'PetFriends')
    )

    driver.find_element(By.CSS_SELECTOR, 'a.nav-link[href="/my_pets"]').click()  # переходим на вкладку Мои Питомцы

    driver.implicitly_wait(10)

    all_my_pets = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')  # Находим всех питомцев в таблице
    all_pets_images = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/th/img')

    assert len(all_my_pets) > 0     # проверяем что список своих питомцев не пуст
    assert len(all_pets_images) > 0

    # Получаем количество питомцев с фото
    pets_with_photo = 0
    for i in range(len(all_pets_images)):
        if all_pets_images[i].get_attribute('src') != '':
            pets_with_photo += 1

    assert len(all_my_pets) / 2 <= pets_with_photo