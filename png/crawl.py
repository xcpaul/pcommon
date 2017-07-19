#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/19 下午10:49
# @Author  : Paul
# @Site    : 
# @Email    : 748067867@qq.com
# @File    : crawl.py
# @Software: PyCharm
import re
import requests
if __name__=="__main__":
	url='http://sbj.saic.gov.cn/sbgg/201611/t20161122_228633.html'
	header={
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate',
		'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,la;q=0.2,ja;q=0.2',
		'Cache-Control':'max-age=0',
		'Connection':'keep-alive',
		# 'Cookie':'sblcookie=20111113; __jsluid=7abf4951b54f33b02757dff7130142a6',
		'Host':'sbj.saic.gov.cn',
		'If-Modified-Since':'Thu, 27 Apr 2017 02:29:17 GMT',
		'If-None-Match':'4fb7-54e1cb9371940-gzip',
		'Referer':'http://sbj.saic.gov.cn/sbgg/index_4.html',
		'Upgrade-Insecure-Requests':'1',
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
	}
	repose=requests.get(url,headers=header)
	html=repose.text
	html=html.encode(repose.encoding).decode('utf-8')

	href=re.compile(r'location.href="(.*?)"')
	result=href.search(html)
	if(result):
		find_url=result.groups()[0]
		print(find_url)
		header={
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding':'gzip, deflate',
			'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,la;q=0.2,ja;q=0.2',
			'Cache-Control':'max-age=0',
			'Connection':'keep-alive',
			'Host':'sbcx.saic.gov.cn:9080',
			'Upgrade-Insecure-Requests':'1',
			'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
		}
		repose=requests.get(find_url,headers=header)
		html=repose.text
		html=html.encode(repose.encoding).decode('utf-8')
		print(html)
