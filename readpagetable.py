from selenium.webdriver.common.by import By

XPATH_TABLE_ROW = "/html/body/div[1]/div[2]/div[3]/form[2]/table[4]/tbody/tr[2]/td/table/tbody/tr"


def create_data_table_list(driver, data_table):  # 현재 페이지의 테이블을 읽음
    table_rows = driver.find_elements(By.XPATH, XPATH_TABLE_ROW)  # 테이블 값을 찾음
    for table_row in table_rows:
        cells = table_row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text for cell in cells]
        data_table.append(row_data)
    return data_table


if __name__ == "__main__":
    import timeit

    SETUP_CODE = """
from selenium import webdriver
driver = webdriver.Chrome(executable_path="chromedriver")
URL = "https://home.kahis.go.kr/home/lkntscrinfo/selectLkntsOccrrncList.do"
driver.get(url=URL)
data_table = []
"""
    TEST_CODE = """
"create_data_table_list(driver=driver, data_table=data_table)"
"""

    result = timeit.timeit(
        stmt=TEST_CODE,
        globals=globals(),
        number=1,
        setup=SETUP_CODE,
    )

    result2 = timeit.timeit(
        stmt=SETUP_CODE,
        globals=globals(),
        number=1,
    )
    print(result, " ", result2)
