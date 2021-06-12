#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.dates as md
import matplotlib.pyplot as plt
# 6.시기별COVID-19신규확진자추이
import pandas as pd
from matplotlib import font_manager

df = pd.read_csv('../rawdata/totally_raw_data_delete_expression.csv', index_col='date')
df.index = df.index.astype(str)
df.index = pd.to_datetime(df.index, format='%Y-%m-%d')

font_path = 'C:\Windows\Fonts\malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font, size=15)

fig, ax = plt.subplots(figsize=(20, 6))
plt.title('시기별 COVID-19 신규 확진자 추이', loc='center', pad=10)
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel('집계일자')
plt.ylabel('신규 확진자 수')
ax.plot(df['i_nw_confirm'], 'hotpink', label='신규 확진자 수')
ax.xaxis.set_major_locator(md.MonthLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%Y-%m-%d'))
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
ax.yaxis.set_major_formatter(md.ticker.StrMethodFormatter('{x:,.0f}'))
ax.set_xlim([df.index[0], df.index[-1]])
plt.legend(loc='upper left')
# plt.show()

plt.savefig('../image/6_시기별COVID-19신규확진자추이.png', dpi=300)
