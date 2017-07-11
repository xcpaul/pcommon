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
browser = webdriver.Chrome()
browser.get("http://cnblogs.com")
time.sleep(1)
browser.find_element_by_link_text("登录").click()
time.sleep(1)
browser.find_element_by_id("input1").send_keys("用户名")
browser.find_element_by_id("input2").send_keys("密码")
browser.find_element_by_id("signin").click()
time.sleep(1)
try:
    if browser.find_element_by_link_text("退出"):
        print("Login Successfully.")
except:
    print("Login failed.")
#browser.quit()