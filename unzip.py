import spider
import os
import gzip
import pandas as pd
from progressbar import ProgressBar

def ungz(path,filename):

    #存储路径
    path_gz = ".\\pdb\\pdb_cif_APS\\"
    #去掉后缀
    f_name = filename.replace(".gz","")

    # 判断文件是否存在，不存在则解压
    isExists=os.path.exists(path_gz+f_name)
    if not isExists:
        #解压
        g_file = gzip.GzipFile(path + "\\" + filename)
        #得到解压后的文件
        open(path_gz + f_name,"wb+").write(g_file.read())
        g_file.close()
    else:
        return

if __name__ == "__main__":

    #压缩文件夹路径
    path = ".\\pdb\\pdb_zip_APS"
    #创建文件夹
    make_path = ".\\pdb\\pdb_cif_APS"
    spider.makedir(make_path)

    #获取文件名 dataframe
    zip_namelist = pd.read_table('./pdb/pdb_name_APS.txt',header = None)

    pbar = ProgressBar()
    for i in pbar(range(len(zip_namelist))):
        #转换文件名
        name_list = zip_namelist.values.tolist() #dataframe > list
        zipName = "".join(name_list[i]) #list > str

        ungz(path,zipName)
    print("解压完成")