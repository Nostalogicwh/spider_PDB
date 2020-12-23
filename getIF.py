from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlrd 
from xlutils.copy import copy 
from progressbar import ProgressBar
import time

def getDetails(i,DOI):
    
    driver.get(url_search)
    #输入搜索内容
    driver.find_element_by_xpath('//*[@id="value(input1)"]').click()
    driver.find_element_by_xpath('//*[@id="value(input1)"]').clear()
    driver.find_element_by_xpath('//*[@id="value(input1)"]').send_keys(DOI)
    
    
    #搜索
    driver.find_element_by_xpath('//*[@id="searchCell1"]/span[1]/button').click()
    
    try:
        #Title
        Title = driver.find_element_by_xpath('//*[@id="RECORD_1"]/div[3]/div/div[1]/div/a/value').text
        excel_table.write(i,2,Title)
        
        #Date
        Date_J = driver.find_element_by_xpath('//*[@id="PublicationYear_tr"]/div/div/div').text
        Date_J = Date_J[0:4]
        excel_table.write(i,4,Date_J)

        #Journal
        Journal = driver.find_element_by_xpath('//*[@id="RECORD_1"]/div[3]/div/div[3]/value').text
        excel_table.write(i,3,Journal)
        
        #进入文章界面
        driver.find_element_by_xpath('//*[@id="RECORD_1"]/div[3]/div/div[1]/div/a/value').click()
    except:
        excel_table.write(i,2,'Error')
        excel_table.write(i,10,'Others')
        return
    

    try:       
        #文献详情
        driver.find_element_by_xpath('//*[@id="show_journal_overlay_link_1"]/p/a').click()
        
        #IF 19年
        IF_19 = driver.find_element_by_xpath('//*[@id="ifactor_1"]/table/tbody/tr[1]/td[1]').text
        excel_table.write(i,5,IF_19)

        #IF 5年
        IF_5 = driver.find_element_by_xpath('//*[@id="ifactor_1"]/table/tbody/tr[1]/td[2]').text
        excel_table.write(i,6,IF_5)

        #JCR® 类别
        JCR_class = driver.find_element_by_xpath('//*[@id="category_1"]/table/tbody/tr[2]/td[1]').text
        excel_table.write(i,7,JCR_class)

        #JCR® 排序
        JCR_rank = driver.find_element_by_xpath('//*[@id="category_1"]/table/tbody/tr[2]/td[2]').text
        excel_table.write(i,8,JCR_rank)

        #JCR partition
        JCR_part = driver.find_element_by_xpath('//*[@id="category_1"]/table/tbody/tr[2]/td[3]').text
        excel_table.write(i,9,JCR_part)

        excel_table.write(i,10,'Web of Science')
        excel.save('PDB_Excel_Diamond.xls')
    except:
        #Title
        print('NoIF')
        excel_table.write(i,10,'Letpub')
        excel.save('PDB_Excel_Diamond.xls')


#获取DOI
def getDOI(i):
    
    return table.cell(i,1).value

#补充web of science中没有的信息
def getDOI_letpub(journal_name):
    url_letpub = 'https://www.letpub.com.cn/index.php?page=journalapp&view=search&searchsort=relevance&searchname='
    driver.get(url_letpub)
    
    #搜索
    try:
        driver.find_element_by_xpath('//*[@id="layui-layer1"]/span[1]/a').click()
    except:
        
        print(journal_name)
        driver.find_element_by_xpath('//*[@id="searchname"]').click()
        driver.find_element_by_xpath('//*[@id="searchname"]').clear()
        driver.find_element_by_xpath('//*[@id="searchname"]').send_keys(journal_name)
        driver.find_element_by_xpath('//*[@id="searchname"]').send_keys(Keys.ENTER)

    time.sleep(5)
    
    return


if __name__ == '__main__':
    #搜索界面链接
    url_search = "http://apps.webofknowledge.com/UA_GeneralSearch_input.do?SID=5Ck7klrD2lnfZN1noaZ&product=UA&search_mode=GeneralSearch"

    #启动浏览器
    driver = webdriver.Chrome('./chromedriver.exe')
    #等待时间
    driver.implicitly_wait(5)

    #选择搜索方式DOI
    driver.get(url_search)
    driver.find_element_by_xpath('//*[@id="select2-select1-container"]').click()
    
    driver.find_element_by_xpath('/html/body/span[27]/span/span[1]/input').send_keys('DOI')
    driver.find_element_by_xpath('/html/body/span[27]/span/span[1]/input').send_keys(Keys.ENTER)


    data = xlrd.open_workbook('PDB_Excel_Diamond.xls',formatting_info=True)
    excel = copy(wb=data) # 完成xlrd对象向xlwt对象转换
    excel_table = excel.get_sheet(0) # 获得要操作的页

    excel_table.write(0,2,'Titel')
    excel_table.write(0,3,'Journal')
    excel_table.write(0,4,'Date')
    excel_table.write(0,5,'IF_19')
    excel_table.write(0,6,'IF_5')
    excel_table.write(0,7,'JCR_class')
    excel_table.write(0,8,'JCR_rank')
    excel_table.write(0,9,'JCR partition')
    excel_table.write(0,10,'Source')


    table = data.sheet_by_index(0)
    nrows = table.nrows # 为行数，整形
    
    #从web of science获取数据
    pbar = ProgressBar()
    for i in pbar(range(nrows)):
        if i == 0:
            continue
        else:
            if table.cell(i,2).value == "":
                DOI = getDOI(i)
                if DOI == 'To be published':
                    continue
                else:
                    getDetails(i,DOI)
            else:
                continue
    
    # #从letpub获取数据
    # pbar = ProgressBar()
    # for i in pbar(range(1, nrows)):
    #     if table.cell(i,10).value == "Letpub":
    #         journal_name = table.cell(i,3).value
    #         getDOI_letpub(journal_name)
    #     else:
    #         continue
    

    excel.save('PDB_Excel_Diamond.xls')