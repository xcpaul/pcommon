#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/10 下午10:28
# @Author  : Paul
# @Site    : 
# @Email    : 748067867@qq.com
# @File    : selenium.py
# @Software: PyCharm
#-*- coding: UTF-8 -*-
from selenium import webdriver
import time
browser = webdriver.Chrome('/Users/Jf/chromedriver')
browser.implicitly_wait(10)
browser.get("http://www.baidu.com")
browser.execute_script("alert('hello world')")
browser.find_element_by_name('request:hnc').send_keys("义乌小商品城")
browser.find_element_by_id('_searchButton').click()
