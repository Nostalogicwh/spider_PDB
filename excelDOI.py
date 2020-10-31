import re
import pandas as pd
from progressbar import ProgressBar
import xlwt
import os
import xlrd
from xlutils.copy import copy
from selenium import webdriver

#网页读取DOI并写入Excel
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
        sheet.write(i+1,1,'To be published')
    excel.save('PDB_Excel.xls')

#cif文件读取DOI写入Excel
def getDOI_2(i,file_name):

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
    sheet.write(i+1,2,str1)


#cif文件中DOI补充
def replace():
    pbar = ProgressBar()
    for i in pbar(range(len(namelist))):

        doi_1 = table.cell(i+1,1).value
        doi_2 = table.cell(i+1,2).value

        if doi_1 == 'None':
            if len(doi_2) > 4:
                sheet.write(i,1,doi_2)
            else:
                continue
        else:
            continue
    
#删除无用数据
def delete():
    for i in range(len(namelist)):
        sheet.write(i,2,'')
    sheet.write(i+1,2,'')

if __name__ == '__main__':
    #文件夹路径
    path = "http://www.rcsb.org/structure/"
    #cif文件名
    namelist = pd.read_table('./pdb/pdb_name.txt',header = None)

    #判断是否存在该Excel文件
    isExists=os.path.exists('./PDB_Excel.xls')
    if not isExists:
        #创建Excel对象
        xls=xlwt.Workbook(encoding='utf-8')
        sheet=xls.add_sheet('PDB')
        sheet.write(0,0,'Name')
        sheet.write(0,1,'DOI')
        #设置第二列宽度
        sheet.col(1).width = 256*32

        #设置第二列宽度
        sheet.col(1).width = 256*32
        xls.save('PDB_Excel.xls')
        data = xlrd.open_workbook('PDB_Excel.xls',formatting_info=True)
        excel = copy(wb=data) # 完成xlrd对象向xlwt对象转换
        sheet = excel.get_sheet(0) # 获得要操作的页
        table = data.sheet_by_index(0)

    else:
        data = xlrd.open_workbook('PDB_Excel.xls',formatting_info=True)
        excel = copy(wb=data) # 完成xlrd对象向xlwt对象转换
        sheet = excel.get_sheet(0) # 获得要操作的页
        table = data.sheet_by_index(0)
    
    #启动浏览器
    driver = webdriver.Chrome('./chromedriver.exe')
    #等待时间
    driver.implicitly_wait(5)

    pbar = ProgressBar()
    for i in pbar(range(len(namelist))):
        #转换文件名
        name_list = namelist.values.tolist() #dataframe > list
        Name = "".join(name_list[i]) #list > str

        #pdb名 
        pdbName = Name.replace(".cif.gz","")
        
        file_name = Name.replace(".gz","")
        #拼接路径
        url = path + pdbName

        getDOI(i,pdbName,url)

        file_name = "./pdb/pdb_cif/" + file_name
        
        getDOI_2(i,file_name)

    delete()



    #保存
    excel.save('PDB_Excel.xls')