#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/6 下午8:18
# @Author  : Paul
# @Site    : 
# @File    : common.py
# @Software: PyCharm
from urllib import request,error
def down(url,num_retries=3):
	try:
		html=request.urlopen(url).read()
		pass
	except error.URLError as e:
		html=None
		if num_retries>0:
			if hasattr(e,'code') and 500<=e.code<600:
				return down(url,num_retries-1)
	except Exception as e:
		html=None
		print(e)
	return html
if __name__=='__main__':

	html=down("http://www.baidu.com")
	print(html)