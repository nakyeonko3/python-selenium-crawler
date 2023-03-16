from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from movepage import check_how_many_number_buttons, move_to_page_by_number_button, move_to_page_by_arrow_button
from showcurrentpagenumber import show_cuttent_page_number
from checkPage import checkIsLastPage, showLastPageNumber
from readpagetable import create_data_table_list
from createcsvfile import create_csv_by_table_list

driver = webdriver.Chrome(executable_path='chromedriver') # 드라이버 인스턴스 생성
URL='https://home.kahis.go.kr/home/lkntscrinfo/selectLkntsOccrrncList.do'
driver.get(url=URL) # URL 초기화
data_table = []

def init(driver, URL='https://home.kahis.go.kr/home/lkntscrinfo/selectLkntsOccrrncList.do'):
    optionSelect = driver.find_element(By.XPATH,' //*[@id="turmGubun2"]')
    optionSelect.click()
    # 발생일 선택

    firstDate = driver.find_element(By.XPATH,' //*[@id="occrFromDtId"]')
    firstDate.click()
    firstDate.send_keys("20160101")
    # 시작일 선택

    lastDate = driver.find_element(By.XPATH,' //*[@id="occrToDtId"]')
    lastDate.click()
    lastDate.send_keys("20221231")
    # 마지막 날짜 선택

    lastDate = driver.find_element(By.XPATH,' //*[@id="btnSearch"]')
    lastDate.click()
    # 조회 버튼 클릭

init(driver)


number_buttons = driver.find_elements(By.XPATH," /html/body/div[1]/div[2]/div[3]/form[2]/table[5]/tbody/tr[2]/td/table/tbody/tr/td[contains(@style,'padding-top:1px')]")
LastPageNumber = showLastPageNumber(driver=driver)

LastPageNumber = 30

executioncount = 0
executionLimit = LastPageNumber / 10 -1

# while not checkIsLastPage(driver = driver):
while True:
    last_number = check_how_many_number_buttons(driver=driver) - 1
    current_number = 0
    create_data_table_list(driver=driver, data_table=data_table)

    
    while current_number < last_number:
        current_number = current_number + 1
        number_buttons = driver.find_elements(By.XPATH," /html/body/div[1]/div[2]/div[3]/form[2]/table[5]/tbody/tr[2]/td/table/tbody/tr/td[contains(@style,'padding-top:1px')]")
        number_buttons[current_number].click()
        create_data_table_list(driver=driver, data_table=data_table)
    try:
        move_to_page_by_arrow_button(driver = driver)
    except:
        print("error")
        print(show_cuttent_page_number(driver=driver))
        move_to_page_by_arrow_button(driver = driver)
        break
    
    executioncount = executioncount + 1
    print(f"executioncount: {executioncount}")
    print(f"if_true?: {executioncount>executionLimit}")
    if executioncount > executionLimit:
        break
    
create_csv_by_table_list(data_table=data_table)


