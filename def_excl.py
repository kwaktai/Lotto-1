import openpyxl
import csv

save_excl = 'D:\\TaiCloud\\Documents\\Project\\Lotto\img\\findstockqty.xlsx'
wb = openpyxl.load_workbook(
    save_excl, data_only=True)
sh1 = wb["text"]
save_text = 'D:\\TaiCloud\\Documents\\Project\\Lotto\img\\mystockdata.tsv'
f = open(save_text, 'r', encoding='utf-8')
rdr = csv.reader(f, delimiter='\t')
r = list(rdr)
try:
    for i in range(0, 20):
        # print(i)
        for p in range(0, 22):
            sh1.cell(row=i+1, column=p+1, value=r[i][p])  # A1에 값쓰기
            # print(r[i][p])
except IndexError:
    pass
f.close()
wb.save(save_excl)

# '''''''''''''''''''''
