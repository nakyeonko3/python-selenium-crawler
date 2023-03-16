from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

URL = 'https://home.kahis.go.kr/home/lkntscrinfo/selectLkntsOccrrncList.do'

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL) 

table_rows = driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div[3]/form[2]/table[4]/tbody/tr[2]/td/table/tbody/tr")

for table_row in table_rows:
    print(table_row.text)
# table row 추출
