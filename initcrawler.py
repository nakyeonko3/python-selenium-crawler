from selenium.webdriver.common.by import By
from selenium import webdriver

from movepage import check_how_many_number_buttons, move_to_page_by_arrow_button

# from showcurrentpagenumber import show_cuttent_page_number
from checkPage import showLastPageNumber
from readpagetable import create_data_table_list
from createcsvfile import create_csv_by_table_list, create_extra_csv_by_table_list


driver = webdriver.Chrome(executable_path="chromedriver")  # 드라이버 인스턴스 생성
URL = "https://home.kahis.go.kr/home/lkntscrinfo/selectLkntsOccrrncList.do"
driver.get(url=URL)  # URL 초기화
data_table = []

XPATH_NEXTPAGE_NUMBER_BUTTONS = " /html/body/div[1]/div[2]/div[3]/form[2]/table[5]/tbody/tr[2]/td/table/tbody/tr/td[contains(@style,'padding-top:1px')]"


def init(driver):
    """발생일, 시작일, 마지막 날짜 를 선택하고 조회 버튼을 클릭"""
    option_select = driver.find_element(By.XPATH, ' //*[@id="turmGubun2"]')
    option_select.click()
    # 발생일 선택

    first_date = driver.find_element(By.XPATH, ' //*[@id="occrFromDtId"]')
    first_date.click()
    first_date.send_keys("20160101")
    # 시작일 선택

    last_date = driver.find_element(By.XPATH, ' //*[@id="occrToDtId"]')
    last_date.click()
    last_date.send_keys("20221231")
    # 마지막 날짜 선택

    last_date = driver.find_element(By.XPATH, ' //*[@id="btnSearch"]')
    last_date.click()
    # 조회 버튼 클릭


init(driver)

Last_page_number = showLastPageNumber(driver=driver)

execution_count = 0
executionLimit = Last_page_number / 10 - 1

# executionLimit = 0

# while not checkIsLastPage(driver = driver):
while True:
    last_number = check_how_many_number_buttons(driver=driver) - 1
    current_number = 0
    create_data_table_list(driver=driver, data_table=data_table)

    while current_number < last_number:
        current_number = current_number + 1
        number_buttons = driver.find_elements(
            By.XPATH,
            XPATH_NEXTPAGE_NUMBER_BUTTONS,
        )
        number_buttons[current_number].click()

        create_data_table_list(driver=driver, data_table=data_table)
        # try:
    move_to_page_by_arrow_button(driver=driver)
    # except:
    #     print("error")
    #     print(show_cuttent_page_number(driver=driver))
    #     move_to_page_by_arrow_button(driver = driver)
    #     break

    execution_count = execution_count + 1
    if execution_count > executionLimit:
        break
    last_number = check_how_many_number_buttons(driver=driver) - 1
    current_number = 0
    create_data_table_list(driver=driver, data_table=data_table)
create_csv_by_table_list(data_table=data_table)

if Last_page_number % 10 > 0:
    last_number = check_how_many_number_buttons(driver=driver) - 1
    current_number = 0
    create_data_table_list(driver=driver, data_table=data_table)

    while current_number < last_number:
        current_number = current_number + 1
        number_buttons = driver.find_elements(
            By.XPATH,
            XPATH_NEXTPAGE_NUMBER_BUTTONS,
        )
        number_buttons[current_number].click()
        create_data_table_list(driver=driver, data_table=data_table)

create_extra_csv_by_table_list(data_table=data_table)
