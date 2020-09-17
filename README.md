11111
# spider_PDB
爬取PDB文件以及相关信息，还不会Markdown，随便写写

# py文件用途介绍

spider.py 爬取下载链接和目标名称，存入pdb文件夹
download.py 将爬取到的cif压缩包下载到pdb/pdb_zip文件夹
unzip.py 将下载好的压缩包解压到pdb/pdb_cif文件夹

# pdb下载链接
http://files.rcsb.org/download/5WYB.pdb

# 没有DOI
to be published 可能已经发表


# cif文件DOI部分不全

# 一些问题
cif文件中DOI 和 PDB网站中DOI不匹配 补全处理
大部分DOI可以用web of science获取信息，部分信息不全用letpub获取，还有部分web of science未收录，需手动处理
多个蛋白质发一篇文章，手动合并 


# 链接： 	搜索条件
# 		diffraction source synchrotron site: SSRF or NFPSS
#		diffraction source synchrotron beamline: BL18U or BL18U1
http://www.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22diffrn_source.pdbx_synchrotron_site%22%2C%22operator%22%3A%22in%22%2C%22negation%22%3Afalse%2C%22value%22%3A%5B%22SSRF%22%2C%22NFPSS%22%5D%7D%2C%22label%22%3A%22input-group%22%2C%22node_id%22%3A0%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22diffrn_source.pdbx_synchrotron_beamline%22%2C%22operator%22%3A%22in%22%2C%22negation%22%3Afalse%2C%22value%22%3A%5B%22BL18U%22%2C%22BL18U1%22%5D%7D%2C%22label%22%3A%22input-group%22%2C%22node_id%22%3A1%7D%5D%7D%5D%2C%22label%22%3A%22text%22%7D%5D%2C%22label%22%3A%22query-builder%22%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22pager%22%3A%7B%22start%22%3A0%2C%22rows%22%3A100%7D%2C%22scoring_strategy%22%3A%22combined%22%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22src%22%3A%22ui%22%2C%22query_id%22%3A%227f7c59abf22077e5de4148e8341e239d%22%7D%7D

# 正则： 要下载的目标
<a class=\"btn btn-default\" type=\"button\" href=\"http://files.rcsb.org/download/(.+?)\" rel=\"noopener noreferrer\">

# 页码xpath正则
/html/body/div[2]/div/div/div[3]/div[2]/div[2]/table/tr/td[2]/div/div[3]/div[1]/div[1]/div[2]/text()[4]
//*[@id="app"]/div[3]/div[2]/div[2]/table/tr/td[2]/div/div[3]/div[1]/div[1]/div[2]
//*[@id="app"]/div[3]/div[2]/div[2]/table/tr/td[2]/div/div[3]/div[1]/div[1]/div[2]/text()[4]

# sys.argv[i]
0 :指程序本身路径
1 :脚本第一个参数
1: :获取到所有的参数，并且输出到一个列表里面。

# 文件类型
txt DataFrame
cif str

http://apps.webofknowledge.com/UA_GeneralSearch_input.do?SID=5Ck7klrD2lnfZN1noaZ&product=UA&search_mode=GeneralSearch
http://apps.webofknowledge.com/Search.do?product=UA&SID=5Ck7klrD2lnfZN1noaZ&search_mode=GeneralSearch&prID=b993fdd0-f5dd-4b4d-aab6-c2f8443cf4ee

# 解决To be published问题
Literature可用信息
	初拟标题
	作者
初步想法：谷歌学术搜索初拟标题，再以作者定位


# 一些有用的信息
NAME
DOI 			_citation.pdbx_database_id_DOI
Method 			_exptl_crystal_grow.method
pH 				_exptl_crystal_grow.pH
Temperature 	_exptl_crystal_grow.temp
Details 		_exptl_crystal_grow.pdbx_details
Classification	_struct_keywords.pdbx_keywords