from selenium.webdriver.common.by import By


XPATH_CURRENT_PAGE_NUMBER = (
    "/html/body/div[1]/div[2]/div[3]/form[2]/table[5]/tbody/tr[2]/td"
)


def show_cuttent_page_number(driver):
    buttons = driver.find_element(By.XPATH, XPATH_CURRENT_PAGE_NUMBER)
    current_button_number = buttons.find_element(By.TAG_NAME, "strong")
    return current_button_number.text
