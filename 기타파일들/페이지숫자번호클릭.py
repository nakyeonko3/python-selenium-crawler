# /html/body/div[1]/div[2]/div[3]/form[2]/table[5]/tbody/tr[2]/td/table/tbody/tr/td[11]


from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium import webdriver
import time

from checkPage import checkIsLastPage


# padding-top:1px



def checkTmpLastPage(driver):
    optionSelect = driver.find_elements(By.XPATH," /html/body/div[1]/div[2]/div[3]/form[2]/table[5]/tbody/tr[2]/td/table/tbody/tr/td[contains(@style,'padding-top:1px')]")
    print(int (optionSelect[-1].text))

if __name__ == "__main__":
    URL = 'https://home.kahis.go.kr/home/lkntscrinfo/selectLkntsOccrrncList.do'
    delayTime = 1 # 클릭후 멈춤 시간

    driver = webdriver.Chrome(executable_path='chromedriver')
    driver.get(url=URL)
    # 초기화
    checkTmpLastPage(driver)
    # for i in optionSelect:
    #     print(int(i.text))
    time.sleep(delayTime)
