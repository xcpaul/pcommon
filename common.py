#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/6 下午8:18
# @Author  : Paul
# @Site    : 
# @File    : common.py
# @Software: PyCharm
import urllib.request
import urllib.error
import urllib.parse
import config
import chardet
import gzip
import re
def p_post(url,data=None,num_retries=3):
	try:
		request_data=b''
		headers_default = config.get_header()
		if data:
			request_data =urllib.parse.urlencode(data).encode('utf-8')

		print("Dowbloading ...",url)
		req = urllib.request.Request(url, headers=headers_default,method="POST")
		response = urllib.request.urlopen(req,data=request_data)
		html=response.read()
		try:
			html=gzip.decompress(html)
		except:
			pass
		chardit1 = chardet.detect(html)
		html=html.decode(chardit1['encoding'])
	except urllib.error.URLError as e:
		print(e)
		html=None
		if num_retries>0:
			if hasattr(e,'code') and 500<=e.code<600:
				return p_post(url,data=data,num_retries=num_retries-1)
	except Exception as e:
		html=None
		print("错误----->",e)
	return html

def p_get(url,data=None,num_retries=3):
	try:
		request_data=b''
		headers_default = config.get_header()
		if data:
			request_data =urllib.parse.urlencode(data).encode('utf-8')

		print("Dowbloading ...",url)
		req = urllib.request.Request(url, headers=headers_default,method="GET")
		response = urllib.request.urlopen(req,data=request_data)
		html=response.read()
		try:
			html=gzip.decompress(html)
		except:
			pass
		chardit1 = chardet.detect(html)
		html=html.decode(chardit1['encoding'])
	except urllib.error.URLError as e:
		print(e)
		html=None
		if num_retries>0:
			if hasattr(e,'code') and 500<=e.code<600:
				return p_get(url,data=data,num_retries=num_retries-1)
	except Exception as e:
		html=None
		print("错误----->",e)
	return html

if __name__=='__main__':

	dazta={
		"p":"12",
	}
	# html=p_post(config.TEST_HTTP_HEADER_POST,data=dazta)
	# fdcontent=re.findall(r'共&nbsp;*(\d*)&nbsp;*页',html)
	html2=p_get(config.TEST_HTTP_HEADER_GET,data=dazta)
	print(html2)
