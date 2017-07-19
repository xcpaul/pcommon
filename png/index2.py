#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/19 下午9:51
# @Author  : Paul
# @Site    : 
# @Email    : 748067867@qq.com
# @File    : index.py
# @Software: PyCharm
import multiprocessing
import requests
from pyquery import PyQuery as pq
import json
def add_sc(url):
	if url.startswith('./'):
		return'http://sbcx.saic.gov.cn:9080/'+url.replace('./','')
	else:
		return url
if __name__ =='__main__':

	files=['index_'+str(u+1)+'.html' for u in range(5)]
	all_links=[]
	for file in files:
		with open(file,'r') as f:
			[all_links.append(add_sc(x)) for x in json.load(f)]
	with open("all_link.txt",'w') as f:
		f.write(json.dumps(all_links))

