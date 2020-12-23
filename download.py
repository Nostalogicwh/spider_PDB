import os
import urllib.request

import pandas as pd
from progressbar import ProgressBar

import spider


def download():
    '''
    下载cif文件到指定路径
    '''
    #路径
    path = "./pdb/pdb_zip_APS/"
    #获取下载路径
    download_linklist = pd.read_table('./pdb/pdb_cif_APS.txt',header = None)
    #获取文件名 dataframe
    download_namelist = pd.read_table('./pdb/pdb_name_APS.txt',header = None)
    pbar = ProgressBar()
    for i in pbar(range(len(download_linklist))):
                
        #转换下载链接
        url_list = download_linklist.values.tolist() #dataframe > list
        urlList = "".join(url_list[i]) #list > str

        #转换文件名
        name_list = download_namelist.values.tolist() #dataframe > list
        urlName = "".join(name_list[i]) #list > str
        # 判断路径是否存在，不存在则下载
        isExists=os.path.exists(path+urlName)
        try:
           if not isExists:
               print('正在下载第' + str(i) + '个')
               urllib.request.urlretrieve(urlList,filename=path+urlName)
           else:
               print('文件已存在')
               pass
        except:
           continue

    #判断是否下载完全
    l = 0
    #获取当前文件数量l
    for lists in os.listdir(path):
        l += 1
    print('当前文件数量：'+str(l))
    if l == len(download_linklist):
        print('下载完毕')
        return
    else:
        print('继续下载')
        download()

if __name__ == "__main__":
    
    #创建文件夹
    make_path=".\\pdb\\pdb_zip_APS"
    spider.makedir(make_path)
    #下载
    download()