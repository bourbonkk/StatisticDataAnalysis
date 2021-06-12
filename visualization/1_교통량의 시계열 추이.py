#!/usr/bin/env python
# coding: utf-8

# In[13]:


# 1.교통량의시계열추이
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
from matplotlib import font_manager

df = pd.read_csv('../rawdata/totally_raw_data_delete_expression.csv', index_col='date')
df.index = df.index.astype(str)
df.index = pd.to_datetime(df.index, format='%Y-%m-%d')

font_path = 'C:\Windows\Fonts\malgun.ttf'
font = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font, size=15)

fig, ax = plt.subplots(figsize=(20, 6))
plt.title('TCS 교통량의 시계열 추이', loc='center', pad=10)
plt.rcParams['axes.unicode_minus'] = False
plt.xlabel('집계일자')
plt.ylabel('교통량(합계)')
ax.plot(df['sm_tot_t'], 'lightskyblue', label='교통량(합계)')
ax.xaxis.set_major_locator(md.MonthLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%Y-%m-%d'))
plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
ax.yaxis.set_major_formatter(md.ticker.StrMethodFormatter('{x:,.0f}'))
ax.set_xlim([df.index[0], df.index[-1]])
plt.legend(loc='upper left')
# plt.show()
plt.savefig('../image/1_교통량의시계열추이.png', dpi=300)
