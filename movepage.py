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
    




