# py文件用途介绍
spider.py 爬取下载链接和目标名称，存入pdb文件夹  
download.py 将爬取到的cif压缩包下载到pdb/pdb_zip文件夹  
unzip.py 将下载好的压缩包解压到pdb/pdb_cif文件夹  
excelDOI.py 将每个蛋白对应的doi号放到excel里  
getIF.py 根据doi号获取文献的一些信息  
editExcel.py 删除重复数据


# pdb下载链接
http://files.rcsb.org/download/5WYB.pdb


# 链接： 	搜索条件
# 		diffraction source synchrotron site: SSRF or NFPSS
#		diffraction source synchrotron beamline: BL18U or BL18U1
http://www.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22diffrn_source.pdbx_synchrotron_site%22%2C%22operator%22%3A%22in%22%2C%22negation%22%3Afalse%2C%22value%22%3A%5B%22SSRF%22%2C%22NFPSS%22%5D%7D%2C%22label%22%3A%22input-group%22%2C%22node_id%22%3A0%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22diffrn_source.pdbx_synchrotron_beamline%22%2C%22operator%22%3A%22in%22%2C%22negation%22%3Afalse%2C%22value%22%3A%5B%22BL18U%22%2C%22BL18U1%22%5D%7D%2C%22label%22%3A%22input-group%22%2C%22node_id%22%3A1%7D%5D%7D%5D%2C%22label%22%3A%22text%22%7D%5D%2C%22label%22%3A%22query-builder%22%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22pager%22%3A%7B%22start%22%3A0%2C%22rows%22%3A100%7D%2C%22scoring_strategy%22%3A%22combined%22%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22src%22%3A%22ui%22%2C%22query_id%22%3A%227f7c59abf22077e5de4148e8341e239d%22%7D%7D


# 2020.12.11修改 
因数据量不足，加入Diamond和APS数据，进行横向比较  
- Diamond
	- 搜索条件及链接
	- diffraction source synchrotron site: Diamond
	- diffraction source synchrotron beamline: I04
	- http://www1.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22operator%22%3A%22exact_match%22%2C%22negation%22%3Afalse%2C%22value%22%3A%22Diamond%22%2C%22attribute%22%3A%22diffrn_source.pdbx_synchrotron_site%22%7D%2C%22node_id%22%3A0%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22operator%22%3A%22exact_match%22%2C%22negation%22%3Afalse%2C%22value%22%3A%22I04%22%2C%22attribute%22%3A%22diffrn_source.pdbx_synchrotron_beamline%22%7D%2C%22node_id%22%3A1%7D%5D%7D%2C%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22operator%22%3A%22greater%22%2C%22negation%22%3Afalse%2C%22value%22%3A%222016-01-01T00%3A00%3A00Z%22%2C%22attribute%22%3A%22rcsb_accession_info.deposit_date%22%7D%2C%22node_id%22%3A2%7D%5D%7D%5D%2C%22label%22%3A%22text%22%7D%5D%2C%22label%22%3A%22query-builder%22%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22pager%22%3A%7B%22start%22%3A0%2C%22rows%22%3A100%7D%2C%22scoring_strategy%22%3A%22combined%22%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22src%22%3A%22ui%22%2C%22query_id%22%3A%22d618e8de8f0eb4edfdfcc821784e3872%22%7D%7D
- APS
	- 搜索条件及链接
	- diffraction source synchrotron site: APS
	- diffraction source synchrotron beamline: 23-ID-D
	- http://www1.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22operator%22%3A%22exact_match%22%2C%22negation%22%3Afalse%2C%22value%22%3A%22APS%22%2C%22attribute%22%3A%22diffrn_source.pdbx_synchrotron_site%22%7D%2C%22node_id%22%3A0%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22operator%22%3A%22exact_match%22%2C%22negation%22%3Afalse%2C%22value%22%3A%2223-ID-D%22%2C%22attribute%22%3A%22diffrn_source.pdbx_synchrotron_beamline%22%7D%2C%22node_id%22%3A1%7D%5D%7D%2C%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22operator%22%3A%22greater%22%2C%22negation%22%3Afalse%2C%22value%22%3A%222016-01-01T00%3A00%3A00Z%22%2C%22attribute%22%3A%22rcsb_accession_info.deposit_date%22%7D%2C%22node_id%22%3A2%7D%5D%7D%5D%2C%22label%22%3A%22text%22%7D%5D%2C%22label%22%3A%22query-builder%22%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22pager%22%3A%7B%22start%22%3A0%2C%22rows%22%3A100%7D%2C%22scoring_strategy%22%3A%22combined%22%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22src%22%3A%22ui%22%2C%22query_id%22%3A%22155778a756965c21400b3dd506a9229f%22%7D%7D 