import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
json_file_name = 'D:\TaiCloud\Documents\Project\stockRpawin_kw\jsop_Key\spreadsheettopython-320114-0340a7e3e1da.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    json_file_name, scope)
gc = gspread.authorize(credentials)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/1kjHe-h2QhXRQNjnt2MDJUIFM_zDelo9ZqeoWhXSmFsE/edit#gid=1309564982'
spreadsheet_url_test = 'https://docs.google.com/spreadsheets/d/1Ihb-0Fg8a9FaHnFADV0YBHBWlXqwpztYiGkSykBiFJE/edit#gid=0'

# 문서 불러오기
doc = gc.open_by_url(spreadsheet_url_test)
# a 시트 불러오기
worksheet = doc.worksheet('시트1')  # 시트선택
cell_data = worksheet.acell('B1').value  # 셀값 가져오기
# row_data = worksheet.row_values(2)#데이터 존재 하는 행까지읽기
# column_data = worksheet.col_values(1) #열읽기

# 범위읽기
# range_list = worksheet.range('A1:D3')
# for cell in range_list:
#     print(cell.value)

# 쓰기
worksheet.update_acell('B1', 'test')
