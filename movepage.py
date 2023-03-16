from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from checkPage import checkIsLastPage
from showcurrentpagenumber import show_cuttent_page_number


def check_how_many_number_buttons(driver):
    number_buttons = driver.find_elements(By.XPATH," /html/body/div[1]/div[2]/div[3]/form[2]/table[5]/tbody/tr[2]/td/table/tbody/tr/td[contains(@style,'padding-top:1px')]")
    return len(number_buttons)

def move_to_page_by_number_button(driver):
    number_buttons = driver.find_elements(By.XPATH," /html/body/div[1]/div[2]/div[3]/form[2]/table[5]/tbody/tr[2]/td/table/tbody/tr/td[contains(@style,'padding-top:1px')]")
    print(len(number_buttons))
    # number_button = driver.find_element(By.XPATH," /html/body/div[1]/div[2]/div[3]/form[2]/table[5]/tbody/tr[2]/td/table/tbody/tr/td[23]")
    # number_button.click()

def move_to_page_by_arrow_button(driver):
    arrow_button = driver.find_element(By.XPATH," /html/body/div[1]/div[2]/div[3]/form[2]/table[5]/tbody/tr[2]/td/table/tbody/tr/td[23]")
    arrow_button.click()
    

# if __name__ == "__main__":
    
#     page_number = 0
#     while not checkIsLastPage(driver = driver):
#         last_number = check_how_many_number_buttons(driver=driver) - 1
#         current_number = 0

#         while current_number < last_number:
#             current_number = current_number + 1
#             number_buttons = driver.find_elements(By.XPATH," /html/body/div[1]/div[2]/div[3]/form[2]/table[5]/tbody/tr[2]/td/table/tbody/tr/td[contains(@style,'padding-top:1px')]")
#             number_buttons[current_number].click()

#         move_to_page_by_arrow_button(driver = driver)

#     page_number = show_cuttent_page_number()
#     print(page_number)




# number_buttons[1].click()
# number_buttons[2].click()
# number_buttons[3].click()
# number_buttons[4].click()
# number_buttons[5].click()
# number_buttons[6].click()
# number_buttons[7].click()
# number_buttons[8].click()
# number_buttons[9].click()



