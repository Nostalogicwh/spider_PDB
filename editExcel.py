import xlwt
import xlrd 
from xlutils.copy import copy 
from progressbar import ProgressBar

data = xlrd.open_workbook('PDB_Excel.xls',formatting_info=True)
excel = copy(wb=data) # 完成xlrd对象向xlwt对象转换
excel_table = excel.get_sheet(0) # 获得要操作的页

table = data.sheet_by_index(0)
nrows = table.nrows # 为行数，整形

pbar = ProgressBar()
for i in pbar(range(nrows)):
    if i == 0:
        continue
    else:
        if table.cell(i,11).value == "":
            continue
        else:
            title = table.cell(i,2).value
            excel_table.write(i,12,title)

            journal = table.cell(i,3).value
            excel_table.write(i,13,journal)

            date = table.cell(i,4).value
            excel_table.write(i,14,date)

            if19 = table.cell(i,5).value
            excel_table.write(i,15,if19)

            if5 = table.cell(i,6).value
            excel_table.write(i,16,if5)

            jcrclass = table.cell(i,7).value
            excel_table.write(i,17,jcrclass)

            jcrrank = table.cell(i,8).value
            excel_table.write(i,18,jcrrank)

            jcrpart = table.cell(i,9).value
            excel_table.write(i,19,jcrpart)

            source = table.cell(i,10).value
            excel_table.write(i,20,source)

excel.save('PDB_Excel.xls')