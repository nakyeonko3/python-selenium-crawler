import pandas as pd

def create_csv_by_table_list(data_table): # 받은 리스트를 csv파일로 바꿔주는 함수
    df = pd.DataFrame(data_table, columns=['Disease', 'Farm', 'Location', 'Date', 'Animal', 'Number', 'Diagnosis', 'End_date'])
    df.to_csv('diseases.csv', index=False)
    

def create_extra_csv_by_table_list(data_table): # 받은 리스트를 csv파일로 바꿔주는 함수
    df = pd.DataFrame(data_table, columns=['Disease', 'Farm', 'Location', 'Date', 'Animal', 'Number', 'Diagnosis', 'End_date'])
    df.to_csv('extra_csv_diseases.csv', index=False)