import xlwt
import xlrd #读
from xlutils.copy import copy #追加写入

#追加写入
data = xlrd.open_workbook('PDB_Excel.xls',formatting_info=True)
excel = copy(wb=data) # 完成xlrd对象向xlwt对象转换
excel_table = excel.get_sheet(0) # 获得要操作的页

#excel_table.write(0,2,'Journy')  
#excel.save('PDB_Excel.xls')


#读取
table = data.sheet_by_index(0)
nrows = table.nrows # 为行数，整形
ncolumns = table.ncols # 为列数，整形
print(nrows)

# 输出某一个单元格值
a = 4
print(table.cell(a,1).value)
print(type(table.cell(a,1).value))

def getDOI(i,pdbname,url):

    driver.get(url)
    try:
        #获取DOI
        DOI = driver.find_element_by_xpath('//*[@id="pubmedDOI"]/a').text

        #写入Excel
        sheet.write(i+1,0,pdbname)
        sheet.write(i+1,1,DOI)
    except:
        sheet.write(i+1,0,pdbname)
        sheet.write(i+1,1,'None')
    excel.save('PDB_Excel.xls')


def getDOI(i,pdbname,file_name):

    txt = ""
    with open(file_name) as file_obj:
        for content in file_obj:
            txt = txt + content

    #正则表达式
    re1 = r"_citation.pdbx_database_id_DOI(.+)"

    #获取DOI
    str1 = re.findall(re1,txt)
    #list>str
    str1 = "".join(str1)
    #去掉左边空格
    str1 = str1.lstrip()
    #写入Excel
    sheet.write(i+1,0,pdbname)
    sheet.write(i+1,1,str1)  