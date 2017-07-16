#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/15 下午11:02
# @Author  : Paul
# @Site    : 
# @Email    : 748067867@qq.com
# @File    : main.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.font_manager import FontManager, FontProperties
from matplotlib import cm

matplotlib.rcParams.update({'font.size': 22})
def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
test_data=[
	{'zwmc':'python 开发1','gsmc':'公司1','zwyx':'3000-6000','sj':'2017-07-15','gzdd':'西安','pc':'40%','jj':'招聘简介11','zw_link':'网页链接1','id':1,'save_date':'2017-07-15'},
	{'zwmc':'python 开发2','gsmc':'公司2','zwyx':'8000-9000','sj':'2017-07-13','gzdd':'杭州','pc':'40%','jj':'招聘简介22','zw_link':'网页链接22','id':2,'save_date':'2017-07-15'},
	{'zwmc':'python 开发555','gsmc':'公司2','zwyx':'8000-4000','sj':'2017-07-12','gzdd':'杭州11','pc':'41%','jj':'招聘简介255','zw_link':'网页链接2234','id':8,'save_date':'2017-07-15'},
	{'zwmc':'python 开发3','gsmc':'公司3','zwyx':'5000-4000','sj':'2017-07-12','gzdd':'杭州11','pc':'41%','jj':'招聘简介255','zw_link':'网页链接2234','id':4,'save_date':'2017-07-15'},
	{'zwmc':'python 开发4','gsmc':'公司4','zwyx':'9000','sj':'2017-07-12','gzdd':'杭州11','pc':'41%','jj':'招聘简介255','zw_link':'网页链接2234','id':9,'save_date':'2017-07-15'}
]
# 指定默认字体
plt.rcParams['axes.unicode_minus'] = False
# 解决保存图像是负号'-'显示为方块的问题
columns = ['zwmc', 'gsmc', 'zwyx', 'sj', 'gzdd', 'pc', 'jj', 'zw_link', 'id', 'save_date']
clean_columns = ['zwmc', 'gsmc', 'zwyx', 'gzdd','pc', 'jj', 'zw_link', 'id', 'save_date']
url_set = set([records['zw_link'] for records in test_data])

df = pd.DataFrame([records for records in test_data], columns=columns)
# columns_update = ['职位名称','公司名称','职位月薪','公布时间','工作地点','反馈率','招聘简介','网页链接','id','信息保存日期']
# df.columns = columns_update
df['save_date'] = pd.to_datetime(df['save_date'])

#2.2 筛选月薪格式为“XXXX-XXXX”的信息
df_clean = df[clean_columns]

# 对月薪的数据进行筛选，选取格式为“XXXX-XXXX”的信息，方面后续分析
# print(df_clean['gz'].str.contains(r'\d+-\d+'))
df_clean = df_clean[df_clean['zwyx'].str.contains(r'\d+-\d+', regex=True)]
print(df_clean)#
print('总行数为：{}行'.format(df_clean.shape[0]))#
# df_clean.head()
#总行数为：22605行


#分割月薪
df_temp=df_clean.copy()
df_temp.loc[: ,'zwyx_min'],df_temp.loc[: , 'zwyx_max'] = df_temp.loc[: , 'zwyx'].str.split('-',1).str#
# 会有警告
s_min, s_max = df_clean.loc[: , 'zwyx'].str.split('-',1).str
df_min = pd.DataFrame(s_min)
df_min.columns = ['zwyx_min']
df_max = pd.DataFrame(s_max)
df_max.columns = ['zwyx_max']

df_clean_concat = pd.concat([df_clean, df_min, df_max], axis=1)
#类型转换
# df_clean_concat['zwyx_min'].astype(int)
# df_clean_concat['zwyx_max'].astype(int)

df_clean_concat['zwyx_min'] = pd.to_numeric(df_clean_concat['zwyx_min'])
df_clean_concat['zwyx_max'] = pd.to_numeric(df_clean_concat['zwyx_max'])
print(df_clean_concat['zwyx_min'].dtype)
df_clean_concat.head(2)

df_clean_concat.sort_values('zwyx_min',inplace=True)
print(df_clean_concat.tail())

# 判断爬取的数据是否有重复值
print(df_clean_concat[df_clean_concat.duplicated('zw_link')==True])



ADDRESS = [ '北京', '上海', '广州', '深圳', '天津', '武汉', '西安', '成都', '大连', '长春', '沈阳', '南京', '济南', '青岛', '杭州', '苏州', '无锡', '宁波', '重庆', '郑州', '长沙', '福州', '厦门', '哈尔滨', '石家庄', '合肥', '惠州', '太原', '昆明', '烟台', '佛山', '南昌', '贵阳', '南宁']
df_city = df_clean_concat.copy()
# 由于工作地点的写上，比如北京，包含许多地址为北京-朝阳区等# 可以用替换的方式进行整理，这里用pandas的replace()方法
for city in ADDRESS:
	df_city['gzdd'] = df_city['gzdd'].replace([(city+'.*')],[city],regex=True)
	# 针对全国主要城市进行分析
df_city_main = df_city[df_city['gzdd'].isin(ADDRESS)]
df_city_main_count = df_city_main.groupby('gzdd')['zwmc','gsmc','jj'].count()
print(df_city_main_count)
df_city_main_count['gsmc'] = df_city_main_count['gsmc']/(df_city_main_count['gsmc'].sum())
df_city_main_count.columns = ['number', 'percentage','ad']#
print(df_city_main_count)
df_city_main_count['label']=df_city_main_count.index+ ' '+ ((df_city_main_count['percentage']*100).round()).astype('int').astype('str')+'%'
# print(type(d


label = df_city_main_count['label']
sizes = df_city_main_count['number']
# 设置绘图区域大小
fig, axes = plt.subplots(figsize=(10,6),ncols=2)
ax1, ax2= axes.ravel()
colors = cm.PiYG(np.arange(len(sizes))/len(sizes))
# colormaps: Paired, autumn, rainbow, gray,spring,Darks#

# 由于城市数量太多，饼图中不显示labels和百分比
patches, texts = ax1.pie(sizes,labels=None, shadow=False, startangle=0, colors=colors)
ax1.axis('equal')
ax1.set_title('城市分布', loc='center')


# ax2 只显示图例（legend）
ax2.axis('off')
ax2.legend(patches, label, loc='center left', fontsize=9)
plt.savefig('job_distribute.jpg')

plt.show()