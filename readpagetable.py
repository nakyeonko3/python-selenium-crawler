from selenium.webdriver.common.by import By

# isPageLeft = True
# count  = 0
# end = 3
    
def create_data_table_list(driver, data_table): # 현재 페이지의 테이블을 읽음
    table_rows = driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div[3]/form[2]/table[4]/tbody/tr[2]/td/table/tbody/tr") #테이블 값을 찾음
    for table_row in table_rows:
        cells = table_row.find_elements(By.TAG_NAME,"td")
        row_data = [cell.text for cell in cells]
        data_table.append(row_data)
    return data_table
        
# while isPageLeft:
#     readCurrentPageTableRows()
#     isPageLeft = not checkIsLastPage(driver=driver) # 마지막 페이지가 아니라면 반복됨
#     count = count + 1
#     if count == end:
#         print(count)
#         isPageLeft = False

# if __name__ == "__main__":
#     init(driver=driver)
#     data_table = create_data_table_list(driver=driver)
#     print(data_table)
#     create_csv_by_table_list(data_table = data_table)

