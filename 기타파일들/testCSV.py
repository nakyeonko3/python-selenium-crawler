import pandas as pd
import time
from datetime import datetime

from initcrawler import init, driver, data_table
from readpagetable import create_data_table_list

init(driver=driver)
create_data_table_list()
