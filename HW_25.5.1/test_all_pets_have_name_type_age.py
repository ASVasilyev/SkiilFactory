from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


"""Проверяет наличие имени, возраста и породы у всех моих питомцев"""


def test_all_mypets_have_name_type_age(driver):
    WebDriverWait(driver, 11).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), 'PetFriends')
    )

    driver.find_element(By.CSS_SELECTOR, 'a.nav-link[href="/my_pets"]').click()  # переходим на вкладку Мои Питомцы

    driver.implicitly_wait(10)

    all_pets_names = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
    all_pets_types = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
    all_pets_ages = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[3]')

    assert len(all_pets_names) > 0
    assert len(all_pets_ages) > 0
    assert len(all_pets_types) > 0
    assert len(all_pets_names) == len(all_pets_ages) == len(all_pets_types)

    result = True
    for i in range(len(all_pets_names)):
        name = all_pets_names[i].text
        age = all_pets_ages[i].text
        type = all_pets_types[i].text

        if name == '': result = False
        if age == '': result = False
        if type == '': result = False

    assert result == True
