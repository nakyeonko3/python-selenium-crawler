from selenium.webdriver.common.by import By


XPATH_NEXTPAGE_NUMBER_BUTTONS = " /html/body/div[1]/div[2]/div[3]/form[2]/table[5]/tbody/tr[2]/td/table/tbody/tr/td[contains(@style,'padding-top:1px')]"
XPATH_NEXTPAGE_ARROW_BUTTON = (
    " /html/body/div[1]/div[2]/div[3]/form[2]/table[5]/tbody/tr[2]/td/table/tbody/tr/td[23]"
)


def check_how_many_number_buttons(driver):
    number_buttons = driver.find_elements(
        By.XPATH,
        XPATH_NEXTPAGE_NUMBER_BUTTONS,
    )
    print(len(number_buttons))
    return len(number_buttons)


def move_to_page_by_number_button(driver):
    number_buttons = driver.find_elements(
        By.XPATH,
        XPATH_NEXTPAGE_NUMBER_BUTTONS,
    )
    print(len(number_buttons))
    # number_button = driver.find_element(By.XPATH," /html/body/div[1]/div[2]/div[3]/form[2]/table[5]/tbody/tr[2]/td/table/tbody/tr/td[23]")
    # number_button.click()


def move_to_page_by_arrow_button(driver):
    arrow_button = driver.find_element(
        By.XPATH,
        XPATH_NEXTPAGE_ARROW_BUTTON,
    )
    arrow_button.click()


if __name__ == "__main__":
    from selenium import webdriver

    driver = webdriver.Chrome(executable_path="chromedriver")  # 드라이버 인스턴스 생성
    URL = "https://home.kahis.go.kr/home/lkntscrinfo/selectLkntsOccrrncList.do"
    driver.get(url=URL)  # URL 초기화
    check_how_many_number_buttons(driver=driver)
