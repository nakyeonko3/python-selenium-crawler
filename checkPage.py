import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver

XPATH_PAGE_NUMBERS_ELEMENT = (
    "/html/body/div[1]/div[2]/div[3]/form[2]/table[5]/tbody/tr[3]/td/table/tbody/tr/td"
)
# 마지막 페이지인지 알려주는 함수, 마지막 페이지라면 True를 출력함
def checkIsLastPage(driver):
    pages = driver.find_element(
        By.XPATH,
        XPATH_PAGE_NUMBERS_ELEMENT,
    )  ##전체 : 829건(1쪽/83쪽)"
    match = re.findall(r"\d+(?=쪽)", pages.text)  # 정규식을 이용해서 추출
    a, b = match
    print(f"{a}/{b}")
    return a == b


# 마지막 페이지 숫자를 알려주는 함수
def showLastPageNumber(driver):
    pages = driver.find_element(
        By.XPATH,
        XPATH_PAGE_NUMBERS_ELEMENT,
    )  ##전체 : 829건(1쪽/83쪽)"
    match = re.findall(r"\d+(?=쪽)", pages.text)  # 정규식을 이용해서 추출
    a, b = match
    print(f"{b}")
    return int(b)


def showCurentPageNumber(driver):
    pages = driver.find_element(
        By.XPATH,
        XPATH_PAGE_NUMBERS_ELEMENT,
    )  ##전체 : 829건(1쪽/83쪽)"
    match = re.findall(r"\d+(?=쪽)", pages.text)  # 정규식을 이용해서 추출
    a, b = match
    return b


# # 테스트
# if __name__ == "__main__":
#     URL = 'https://home.kahis.go.kr/home/lkntscrinfo/selectLkntsOccrrncList.do'
#     driver = webdriver.Chrome(executable_path='chromedriver')
#     driver.get(url=URL)
#     print(showLastPageNumber(driver=driver))
