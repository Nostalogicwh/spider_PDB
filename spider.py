from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
from lxml import etree

import numpy as np
import pandas as pd

import re
import time

import os

'''
搜索条件
diffraction source synchrotron site: SSRF or NFPSS
diffraction source synchrotron beamline: BL18U or BL18U1
'''
URL = 'http://www.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22diffrn_source.pdbx_synchrotron_site%22%2C%22operator%22%3A%22in%22%2C%22negation%22%3Afalse%2C%22value%22%3A%5B%22SSRF%22%2C%22NFPSS%22%5D%7D%2C%22label%22%3A%22input-group%22%2C%22node_id%22%3A0%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22diffrn_source.pdbx_synchrotron_beamline%22%2C%22operator%22%3A%22in%22%2C%22negation%22%3Afalse%2C%22value%22%3A%5B%22BL18U%22%2C%22BL18U1%22%5D%7D%2C%22label%22%3A%22input-group%22%2C%22node_id%22%3A1%7D%5D%7D%5D%2C%22label%22%3A%22text%22%7D%5D%2C%22label%22%3A%22query-builder%22%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22pager%22%3A%7B%22start%22%3A0%2C%22rows%22%3A100%7D%2C%22scoring_strategy%22%3A%22combined%22%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22src%22%3A%22ui%22%2C%22query_id%22%3A%227f7c59abf22077e5de4148e8341e239d%22%7D%7D'

def downloadink():
    '''
    将下载链接写入文件
    '''

    #设立并清空文件
    filename_cif = './pdb/pdb_cif.txt'
    with open(filename_cif,'w') as f:
        f.truncate()
    
    filename_name = './pdb/pdb_name.txt'
    with open(filename_name,'w') as f:
        f.truncate()

    #获取页码
    time.sleep(3)
    source = driver.page_source
    page = re.findall(r'<div style=\"display: inline-block; vertical-align: top; line-height: 27.5px; padding: 0px 30px;\">Page 1 of (.+?)</div>',source)
    page = int(page[1]) + 1

    for i in range(1,page):
        #等待加载
        time.sleep(3)

        #获取网页源代码
        source = driver.page_source 

        #正则匹配下载链接
        linklist = re.findall(r'<a class=\"btn btn-default\" type=\"button\" href=\"http://files.rcsb.org/download/(.+?)\" rel=\"noopener noreferrer\"',source)

        #将数据写入文件
        for link in linklist: 
            with open(filename_cif,'a') as f:
                f.write('http://files.rcsb.org/download/'+link+'\n')
            with open(filename_name,'a') as f:
                f.write(link+'\n')
        
        # 匹配翻页链接
        page_next = driver.find_elements("css selector",".srch-btn")
        print(page_next[9].text)
        page_next[9].click()
        i += 1
    return

   

def makedir(path):
    '''
    创建文件夹
    '''
 
    # 判断路径是否存在
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path) 
        return True
    else:
        # 如果目录存在则不创建
        return False

if __name__ == '__main__':
    
    #运行chrome
    driver = webdriver.Chrome('./chromedriver.exe')

    #加载页面
    driver.get(URL)

    #爬取下载链接
    downloadink()

    #读取下载链接
    download_linklist = pd.read_table('./pdb/pdb_cif.txt',header = None)
    print(download_linklist)
    
    #退出
    driver.quit()